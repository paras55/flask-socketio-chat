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
	
	#print('Message: ' + msg)
	if (msg=='hey'):
		send("hiiiiiiii")
 	else :
    		send("fck you")

		
	'''print('Message: ' + msg) # this message is printed in server of colab 
	ok='message received'
	send(ok, broadcast=True) # this ok is printed in chatbox , whatever you send from here is printed in chat'''

if __name__ == '__main__':
  app.run()
  socketio.run( app, debug = True )
  
