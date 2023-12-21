from flask import Flask, render_template, request, send_from_directory, url_for, jsonify
from database import get_blogs_from_mongodb, get_news_from_mongodb, get_executives_from_mongodb, get_community_service_from_mongodb, get_blog_by_name


blog_data = get_blogs_from_mongodb()
print(blog_data[0]['images'][0]['url'])
community_service_data = get_community_service_from_mongodb()
executives_data = get_executives_from_mongodb()
news_data = get_news_from_mongodb()



app = Flask(__name__)

def process_images(image_data):
    if image_data:
        image_pairs = [pair.split() for pair in image_data.split(',')]
        images = [{"url": pair[0], "alt": pair[1] if len(pair) > 1 else ""} for pair in image_pairs]
        return images
    else:
        return []

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            "name": request.form.get('name').replace(" ", "_"),
            "title": request.form.get('title'),
            "content": request.form.get('content'),
            "date": request.form.get('date'),
            "images": process_images(request.form.get('image_data')),
        }
        return render_template('create.html', data=data)
    else:
        return render_template('create.html')

@app.route('/')
def index():
    current_page = '/'
    return render_template('index.html', current_page=current_page, event_data=blog_data, community_service_data=community_service_data)

@app.route('/about')
def about():
    current_page = '/about'
    return render_template('about.html', current_page=current_page, executives_data=executives_data, event_data=blog_data)

@app.route('/events')
def events():
    current_page = '/events'
    return render_template('event.html', current_page=current_page, event_data=blog_data, community_service_data=community_service_data)

@app.route('/publications')
def publications():
    current_page = '/publications'
    return render_template('publish.html', current_page=current_page, event_data=blog_data)

@app.route('/news')
def news():
    current_page = '/news'
    return render_template('news.html', current_page=current_page, news_data=news_data, event_data=blog_data)

@app.route('/membership')
def membership():
    current_page = '/membership'
    return render_template('membership.html', current_page=current_page, event_data=blog_data)

@app.route('/contact')
def contact():
    current_page = '/contact'
    return render_template('contact.html', current_page=current_page, event_data=blog_data, executives_data=executives_data)

@app.route('/blog/<string:page_name>')
def blog_page(page_name):
    # Fetch blog data
    blogs_data = get_blog_by_name(page_name)
    
    # Check if the blog exists
    if blog_data:
        # Pass the blog data to the template
        return render_template('blogpage.html', date = blogs_data['date'] ,title=blogs_data['title'], content=blogs_data['content'], images=blogs_data['images'], blogs_data=blogs_data, event_data=blog_data)
    else:
        # Render a template for a blog not found
        return render_template('blog_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
