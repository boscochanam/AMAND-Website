from flask import Flask, render_template, request, send_from_directory, url_for
from database import get_events_from_mongodb

app = Flask(__name__)

@app.route('/')
def index():
    current_page = '/'
    print(current_page)
    event_data = get_events_from_mongodb()
    print(event_data)
    return render_template('index.html', current_page=current_page, event_data=event_data)

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

if __name__ == "__main__":
    app.run()
