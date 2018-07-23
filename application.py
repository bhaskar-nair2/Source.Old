from flask import Flask, render_template, session, request, flash, jsonify
from flask_socketio import SocketIO, emit
from passhash import Hasher
from mongoslave import MongoConnect
from search import Search

app = Flask(__name__)
app.secret_key = b"de$Tps%qPQ@345jDkoMOuYouKnowWhat?JustFuckOff"
app.config.from_pyfile('config.cfg')
Mongo = MongoConnect(app)
socketio = SocketIO(app)
socketio.init_app(app)


# ROUTE HANDLERS
@app.route('/')
@app.route('/<username>')
def index(username=None):
    return render_template('index.html', user=username)


@app.route('/search', methods=['POST'])
def search():
    return render_template('results.html')


@app.route('/downloads')
@app.route('/downloads/<username>')
def downloads(username=None):
    return render_template('downloads.html', user=username)


@app.route("/uploads/<username>", methods=['GET', 'POST'])
def upload(username):
    if request.method == 'POST':
        return 'POST: uploads'
    else:
        return "GET: uploads"


@app.route("/pages")
@app.route("/pages/<pageID>")
def page(pageID=None):
    return render_template('sub-page.html', pageID=pageID)


@app.route('/namecheck', methods=['POST'])
def check():
    return True


# SOCKET HANDLERS
@socketio.on('signup')
def signup(data):
    if Mongo.checkUser(data[0]):
        # try:
        x = Hasher.build(data[0], data[2], app.secret_key)
        Mongo.insert('source_credentials', {"user": x[0], "password": x[1], "mail": data[1]})
        session['user'] = x[0]
        return emit('signedup', jsonify(bool=True, msg='Signed-Up'), json=True)
    else:
        return emit('signedup', jsonify(bool=False, msg='Username Taken'), json=True)


@socketio.on('login')
def login(data):
    print('1')
    re = Mongo.getUser(data[0])
    if re:
        if Hasher.retrive(app.secret_key, data[0], data[1], re[1]):
            session['user'] = data[0]
            return emit('loggedin', {'bool': True, 'msg': 'Login Successful'}, json=True)
        else:
            return emit('loggedin', {'bool': False, 'msg': 'Data Seems to be invalid'}, json=True)
    else:
        return emit('loggedin', {'bool': False, 'msg': 'Data Seems to be invalid'}, json=True)


@socketio.on('init')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('name_check')
def handle_name(data):
    socketio.emit('responded', Mongo.checkUser(data))


@socketio.on('search')
def search(data):
    obj = Search(data)
    dat = obj.search()
    if dat is not None:
        print(dat)
        return emit('objects', dat, json =True)


# ERROR HANDLERS
@app.errorhandler(404)
def er404(e):
    return render_template('error.html', error='404')


@app.errorhandler(500)
def er500(e):
    return render_template('error.html', error='500')


if __name__ == '__main__':
    app.run()
