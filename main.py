from flask import Flask, render_template
from flask_socketio import SocketIO, emit,send
from flask_ngrok import run_with_ngrok

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)
run_with_ngrok(app) 

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )


@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
  app.run()
  socketio.run( app, debug = True )
  
