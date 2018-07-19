from flask import Flask, render_template, session, request, flash
from passhash import Hasher
from mongoslave import MongoConnect

application = Flask(__name__)
application.secret_key = b"\xd0\t\xc4#lM`2;c\x14T3^\x02\xd7y\x81wYouKnowWhat?JustFuckOff"
application.config.from_pyfile('config.cfg')
Mongo=MongoConnect(application)

@application.route('/')
@application.route('/<username>')
def index(username=None):
    return render_template('index.html')


@application.route('/search', methods=['POST'])
def search():
    return render_template('results.html')


@application.route('/downloads')
@application.route('/downloads/<username>')
def downloads(username=None):
    return render_template('downloads.html')


@application.route("/uploads/<username>", methods=['GET', 'POST'])
def upload(username):
    if request.method == 'POST':
        return 'POST: uploads'
    else:
        return "GET: uploads"


@application.route("/pages")
@application.route("/pages/<pageID>")
def page(pageID=None):
    return render_template('sub-page.html',pageID=pageID)


@application.route('/signup', methods=['POST'])
def signup():
    x = Hasher.build(request.form['signup-user'], request.form['signup-pass'], application.secret_key)
    Mongo.insert('source-credentials',{"x":1})
    return 'Signed Up'


@application.route('/login', methods=['POST'])
def login():
    return 'Logged In'

@application.route('/namecheck', methods=['POST'])
def check():
    return True


@application.errorhandler(404)
def er404(e):
    return render_template('error.html', error='404')


@application.errorhandler(500)
def er500(e):
    return render_template('error.html', error='500')


if __name__ == '__main__':
    application.run()
