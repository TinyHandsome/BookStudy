import sys
import asyncio

from charfinder import UnicodeNameIndex #1

CRLF = b'\r\n'
PROMPT = b'?>'

index = UnicodeNameIndex() #2

@asyncio.coroutine
def handle_queries(reader, writer): #3
    while True: #4
        writer.write(PROMPT) # 不能使用yield from #5
        yield from writer.drain() # 必须使用 yield from #6
        data = yield from reader.readline() #7
        try:
            query = data.decode().strip()
        except UnicodeDecodeError: #8
            query = '\x00'
        client = writer.get_extra_info('peername') #9
        print('Received from {}: {!r}'.format(client, query)) #10
        if query:
            if ord(query[:1]) < 32: #11
                break
            lines = list(index.find_description_strs(query)) #12
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines) #13
            writer.write(index.status(query, len(lines)).encode() + CRLF) #14
            
            yield from writer.drain() #15
            print('Sent {} results'.format(len(lines))) #16
        
        print('Close the client socket') #17
        writer.close() #18
        
def main(address='127.0.0.1', port=2323): #1
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port, loop=loop) #2
    server = loop.run_until_complete(server_coro) #3
    host = server.sockets[0].getsockname() #4
    print('Serving on {}. Hit CTRL-C to stop.'.format(host)) #5
    try:
        loop.run_forever() #6
    except KeyboardInterrupt: # 按CTRL-C键
        pass
    
    print('Server shutting down.')
    server.close() #7
    loop.run_until_complete(server.wait_closed()) #8
    loop.close() #9

if __name__ == '__main__':
    main(*sys.argv[1:]) #10