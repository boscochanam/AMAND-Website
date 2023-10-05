from flask import Flask, render_template, request, send_from_directory, url_for

app = Flask(__name__)

@app.route('/')
def index():
    current_page = '/'
    print(current_page)
    return render_template('index.html', current_page=current_page)

@app.route('/about')
def about():
    current_page = '/about'
    print(current_page)
    return render_template('about.html', current_page=current_page)

@app.route('/events')
def events():
    current_page = '/events'
    return render_template('event.html', current_page=current_page)

@app.route('/publications')
def publications():
    current_page = '/publications'
    return render_template('publish.html', current_page=current_page)

@app.route('/news')
def news():
    current_page = '/news'
    return render_template('news.html', current_page=current_page)

@app.route('/membership')
def membership():
    current_page = '/membership'
    return render_template('membership.html', current_page=current_page)

@app.route('/contact')
def contact():
    current_page = '/contact'
    return render_template('contact.html', current_page=current_page)

@app.route('/static/images/<path:image_filename>')
def serve_image(image_filename):
    return send_from_directory('static/images', image_filename)

@app.route('/gallery')
def gallery():
    images = [
        {
            'url': url_for('serve_image', image_filename='cause-1.jpg'),
            'title': "Patriot's Day 2023",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        {
            'url': url_for('serve_image', image_filename='cause-2.jpg'),
            'title': "Manipur Protest",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        {
            'url': url_for('serve_image', image_filename='cause-3.jpg'),
            'title': "International Women's Day",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        {
            'url': url_for('serve_image', image_filename='cause-4.jpg'),
            'title': "AMAND Calendar Release 2023",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        {
            'url': url_for('serve_image', image_filename='cause-5.jpg'),
            'title': "Ningol Chakouba 2023",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        {
            'url': url_for('serve_image', image_filename='cause-6.jpg'),
            'title': "Patriot's Day 2022",
            'description': "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life",
            'date': "1 Jan 2023"
        },
        # Add more events here
    ]
    return render_template('events.html', images=images)

if __name__ == "__main__":
    app.run()
