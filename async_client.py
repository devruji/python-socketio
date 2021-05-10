import asyncio
import sys
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connected')
    result = await sio.call('sum', {'numbers': [1, 2]})
    print(result)

@sio.event
async def connection_error(e):
    print(e)

@sio.event
async def disconnect():
    print('disconnected')

@sio.event
async def mult(data):
    return data['numbers'][0] * data['numbers'][1]

@sio.event
async def client_count(count):
    print('There are', count, 'connected clients.')

@sio.event
async def room_count(count):
    print('There are', count, 'clients in my room.')

@sio.event
async def user_joined(username):
    print(f'User {username} has joined')

@sio.event
async def user_left(username):
    print(f'User {username} has left')

async def main(username):
    await sio.connect(url='http://localhost:8000',
                headers={'X_Username': username})

    await sio.wait()

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)