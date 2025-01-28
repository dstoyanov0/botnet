import socket, asyncio

async def admin_cmd(cmd):
    pass

async def bot_cmd(cmd):
    if cmd == 'get':
        pass
    elif cmd.split('|')[0] == 'login':
        pass
    elif cmd.split('|')[0] == 'status':

async def handle_client(conn, addr):
    loop = asyncio.get_event_loop()
    request = None
    access = 'bot'
    while request != 'quit':
        request = (await loop.sock_recv(conn, 255)).decode('utf8').split('\n')[0]
        response = 'error.access-level'
        if request == 'sudo su':
            access = 'admin'
            response = 'Hello Admin!'
        elif access == 'admin':
            response = await admin_cmd(request)
        elif access == 'bot':
            response = await bot_cmd(request)
        await loop.sock_sendall(conn, bytes(response+'\n', 'utf8'))
    conn.close()

async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1111))
    server.listen(8)
    server.setblocking(False)
    loop = asyncio.get_event_loop()
    while True:
        client, addr = await loop.sock_accept(server)
        loop.create_task(handle_client(client, addr))

if __name__ == '__main__':
    asyncio.run(main())
