from flask import Flask, render_template, request, send_from_directory, url_for
from database import get_events_from_mongodb, get_news_from_mongodb, get_executives_from_mongodb, get_community_service_from_mongodb

app = Flask(__name__)

@app.route('/')
def index():
    current_page = '/'
    print(current_page)
    event_data = get_events_from_mongodb()
    community_service_data = get_community_service_from_mongodb()
    print(event_data)
    return render_template('index.html', current_page=current_page, event_data=event_data, community_service_data=community_service_data)

@app.route('/about')
def about():
    current_page = '/about'
    event_data = get_events_from_mongodb()
    executives_data = get_executives_from_mongodb()
    print(current_page)
    return render_template('about.html', current_page=current_page, executives_data=executives_data, event_data=event_data)

@app.route('/events')
def events():
    current_page = '/events'
    event_data = get_events_from_mongodb()
    community_service_data = get_community_service_from_mongodb()
    return render_template('event.html', current_page=current_page, event_data=event_data, community_service_data=community_service_data)

@app.route('/publications')
def publications():
    event_data = get_events_from_mongodb()
    current_page = '/publications'
    return render_template('publish.html', current_page=current_page, event_data = get_events_from_mongodb())

@app.route('/news')
def news():
    event_data = get_events_from_mongodb()
    current_page = '/news'
    news_data = get_news_from_mongodb()
    return render_template('news.html', current_page=current_page, news_data=news_data, event_data=event_data)

@app.route('/membership')
def membership():
    event_data = get_events_from_mongodb()
    current_page = '/membership'
    return render_template('membership.html', current_page=current_page, event_data = event_data)

@app.route('/contact')
def contact():
    event_data = get_events_from_mongodb()
    current_page = '/contact'
    return render_template('contact.html', current_page=current_page, event_data = event_data)


if __name__ == "__main__":
    app.run()
