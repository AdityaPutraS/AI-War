import asyncio
from config import config

success_message = 'Success'
failed_message = 'Failed'


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))
        splitMessage = message.split(' ')
        if('URO' in splitMessage):
            namaRobot = splitMessage[1]
            aksi = splitMessage[2]
            # aksi = maju, putar, majuPutar, tembak (otw)
            param1 = int(splitMessage[3])
            # param1 = banyak maju, sudut putar, untuk majuPutar param1 = banyakMaju, tembak -> param = 0
            param2 = 0
            if(len(splitMessage) == 5 and aksi == 'majuPutar'):
                param2 = int(splitMessage[4])
            if(namaRobot in config.namaRobot):
                if(aksi == 'maju'):
                    config.robot[config.namaRobot[namaRobot]].maju(param1)
                    await asyncio.sleep(1)
                    writer.write(data)
                elif(aksi == 'putar'):
                    config.robot[config.namaRobot[namaRobot]].putar(param1)
                    await asyncio.sleep(1)
                    writer.write(data)
                elif(aksi == 'majuPutar'):
                    config.robot[config.namaRobot[namaRobot]].majuPutar(param1,param2)
                    await asyncio.sleep(1)
                    writer.write(data)
                elif(aksi == 'tembak'):
                    pass
                else:
                    writer.write(data)
        else:
            print("Send: %r" % message)
            writer.write(data)
        await writer.drain()
    print("Close the client socket")
    writer.close()

def startServerURO():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
