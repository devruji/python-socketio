import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

def task(sid):
    sio.sleep(3)
    result = sio.call('mult', {'numbers': [3, 4]}, to=sid)
    
    print(result)

@sio.event
def connect(sid, environ): #SessionId random(string)
    print(sid, 'connected')

    sio.start_background_task(task, sid)

@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]

    # sio.emit('sum_result', {'result': result}, to=sid)

    return {'result': result}