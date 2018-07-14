from flask import Flask, render_template, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key= 'youKnowWhatJustFuckOff'
app.config.from_pyfile('config.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    return 'Hello World'


@app.route('/downloads')
def downloads():
    return render_template('downloads.html')

@app.route('/signup', methods=['POST'])
def signup():
    return 'Signed Up'


@app.route('/login', methods=['POST'])
def login():
    return 'Logged In'


if __name__ == '__main__':
    app.run()
