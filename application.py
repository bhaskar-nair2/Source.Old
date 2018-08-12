from flask import Flask, render_template, session, request, flash, jsonify, redirect, url_for
from flask_socketio import SocketIO, emit
from passhash import Hasher
from slaves import MongoConnect, SQLConnect
from search import Search

app = Flask(__name__)
app.secret_key = b"de$Tps%qPQ@345jDkoMOuYouKnowWhat?JustFuckOff"
app.config.from_pyfile('config.cfg')
Mongo = MongoConnect(app)
socketio = SocketIO(app)
socketio.init_app(app)
SQL = SQLConnect()


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
    SQLItem = ('Machine Learning', 'CS103', 'SWE')
    id = SQL.addSub(SQLItem)
    MongoItem = {'sub_id': id, 'sub_name': 'Machine Learning', 'sub_code': 'CS103', 'department': 'SWE',
                 'redirect_codes': ['12CS103', '13CS102'], 'teachers': ['Sunita', 'Punita', 'Chunita'],
                 'bundles': [{'bundle_id': '112', 'bundle_name': 'PassMePlz', 'author': 'gandu mara',
                              'bundle_desc': 'Gand mari Meri', 'bundle_link': 'www.lalal.com',
                              'bundle_downloads': 13, 'bundle_rating': 3.67}],
                 'files': [{'file_id': '11', 'filename': 'gobar', 'author': 'lodaSingh', 'format': 'PDF',
                            'file_link': 'www.dd.com', 'file_rating': 4}],
                 'video_links': ['www.dd.com']}
    Mongo.addSub(MongoItem)
    return render_template('downloads.html', user=username)


@app.route("/uploads/<username>", methods=['GET', 'POST'])
def upload(username):
    if request.method == 'POST':
        return 'POST: uploads'
    else:
        return "GET: uploads"


@app.route("/subjects")
@app.route("/subjects/<int:subjectID>", methods=['GET', 'POST'])
def subjects(subjectID=None):
    if subjectID:
        return render_template('sub-page.html', sub=Mongo.subdesc(subjectID))
    else:
        return render_template('sub-list-page.html', subList=SQL['subjects'])


@app.route('/contribute/<int:subID>')
def contribute(subID=None):
    return "Nice" + str(subID)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    flash("Logged Out")
    return redirect(url_for('index'))


# SOCKET HANDLERS
@socketio.on('signup')
def signup(data):
    if Mongo.checkUser(data[0]):
        # try:
        x = Hasher.build(data[0], data[2], app.secret_key)
        Mongo.addUser({"user": x[0], "password": x[1], "mail": data[1]})
        session['user'] = x[0]
        return emit('signedup', jsonify(bool=True, msg='Signed-Up'), json=True)
    else:
        return emit('signedup', jsonify(bool=False, msg='Username Taken'), json=True)


@socketio.on('login')
def login(data):
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
        obj.terminate()
        return emit('objects', dat, json=True)


# ERROR HANDLERS
@app.errorhandler(404)
def er404(e):
    return render_template('error.html', error='404')


@app.errorhandler(500)
def er500(e):
    return render_template('error.html', error='500')


if __name__ == '__main__':
    app.run(debug=True)
