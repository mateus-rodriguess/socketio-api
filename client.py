import socketio

sio = socketio.Client()


@sio.event()
def connect():
    print("connection established")



@sio.on("message")
def message(data):
    print("message: ", data)


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://127.0.0.1:8080/")
sio.wait()
