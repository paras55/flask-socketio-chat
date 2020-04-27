from flask import Flask 
from flask_ngrok import run_with_ngrok

from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
run_with_ngrok(app) 


@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run( app, debug = True )
  	app.run()
