from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    current_page = '/'
    return render_template('index.html', current_page=current_page)

@app.route('/about')
def about():
    current_page = '/about'
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

if __name__ == "__main__":
    app.run()
