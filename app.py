from flask import Flask, render_template, request, send_from_directory, url_for
from database import get_events_from_mongodb, get_news_from_mongodb, get_executives_from_mongodb, get_community_service_from_mongodb, get_blog_by_name

app = Flask(__name__)

# Fetch data once when the application starts
event_data = get_events_from_mongodb()
community_service_data = get_community_service_from_mongodb()
executives_data = get_executives_from_mongodb()
news_data = get_news_from_mongodb()

@app.route('/')
def index():
    current_page = '/'
    return render_template('index.html', current_page=current_page, event_data=event_data, community_service_data=community_service_data)

@app.route('/about')
def about():
    current_page = '/about'
    return render_template('about.html', current_page=current_page, executives_data=executives_data, event_data=event_data)

@app.route('/events')
def events():
    current_page = '/events'
    return render_template('event.html', current_page=current_page, event_data=event_data, community_service_data=community_service_data)

@app.route('/publications')
def publications():
    current_page = '/publications'
    return render_template('publish.html', current_page=current_page, event_data=event_data)

@app.route('/news')
def news():
    current_page = '/news'
    return render_template('news.html', current_page=current_page, news_data=news_data, event_data=event_data)

@app.route('/membership')
def membership():
    current_page = '/membership'
    return render_template('membership.html', current_page=current_page, event_data=event_data)

@app.route('/contact')
def contact():
    current_page = '/contact'
    return render_template('contact.html', current_page=current_page, event_data=event_data, executives_data=executives_data)

@app.route('/blog/<string:page_name>')
def blog_page(page_name):
    # Fetch blog data
    blog_data = get_blog_by_name(page_name)
    
    # Check if the blog exists
    if blog_data:
        # Pass the blog data to the template
        return render_template('blogpage.html', title=blog_data['title'], content=blog_data['content'], images=blog_data['images'], event_data=event_data)
    else:
        # Render a template for a blog not found
        return render_template('blog_not_found.html')

if __name__ == "__main__":
    app.run()
