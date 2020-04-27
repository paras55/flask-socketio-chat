<html>
<head>
<title>Chat Room</title>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.8/socket.io.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
</head>
<body>
<script type="text/javascript">
$(document).ready(function() {

	var socket = io.connect( 'http://' + document.domain + ':' + location.port );

	socket.on('connect', function() {
		socket.send('User has connected!');
	});

	socket.on('message', function(msg) {
		$("#messages").append('<li>'+msg+'</li>');
		console.log('Received message');
	});

	$('#sendbutton').on('click', function() {
		socket.send($('#myMessage').val());
		$('#myMessage').val('');
	});

});
</script>
<ul id="messages"></ul>
<input type="text" id="myMessage">
<button id="sendbutton">Send</button>
</body>
</html>