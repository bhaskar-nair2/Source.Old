from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

socketio.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my_event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('name_check')
def handle_my_custom_event(data):
    print(str(data))
    socketio.emit('responded', 'Nice!')


def ack():
    print('message was received!')


if __name__ == '__main__':
    app.run()
