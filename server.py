import asyncio
from config import config

success_message = 'Success'
failed_message = 'Failed'
sleep_duration = 0.8

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
            param1 = float(splitMessage[3])
            # param1 = banyak maju, sudut putar, untuk majuPutar param1 = banyakMaju, tembak -> param = 0
            param2 = 0
            if(len(splitMessage) == 5 and aksi == 'majuPutar'):
                param2 = float(splitMessage[4])
            if(namaRobot in config.namaRobot):
                if(aksi == 'maju'):
                    config.robot[config.namaRobot[namaRobot]].maju(param1)
                    await asyncio.sleep(sleep_duration)
                    writer.write(success_message.encode())
                elif(aksi == 'putarCW'):
                    if(param1 >= 0):
                        config.robot[config.namaRobot[namaRobot]].putarCW(param1)
                        await asyncio.sleep(sleep_duration)
                        writer.write(success_message.encode())
                    else:
                        writer.write(failed_message.encode())
                elif(aksi == 'putarCCW'):
                    if(param1 >= 0):
                        config.robot[config.namaRobot[namaRobot]].putarCCW(param1)
                        await asyncio.sleep(sleep_duration)
                        writer.write(success_message.encode())
                    else:
                        writer.write(failed_message.encode())
                elif(aksi == 'majuPutar'):
                    config.robot[config.namaRobot[namaRobot]].majuPutar(param1,param2)
                    await asyncio.sleep(sleep_duration)
                    writer.write(success_message.encode())
                elif(aksi == 'tembak'):
                    pass
                elif(aksi == 'status'):
                    r = config.robot[config.namaRobot[namaRobot]]
                    x,y = r.getPosisi()
                    arah = r.getArah()
                    hp = r.getHP()
                    am = r.getAmmo()
                    status = '%d %d %.2f %.2f %d' % (x,y,arah,hp,am)
                    writer.write(status.encode())
                else:
                    writer.write(failed_message.encode())
            else:
                if(aksi == 'buat'):
                    if(config.addNewRobot(namaRobot)):
                        writer.write(success_message.encode())
                    else:
                        writer.write(failed_message.encode())
        else:
            print("Input tidak dikenal, input : %r" % message)
            writer.write(failed_message.encode())
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
