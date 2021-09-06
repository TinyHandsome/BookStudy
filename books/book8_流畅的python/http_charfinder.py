from aiohttp import web
import asyncio, sys


def home(request): #1
    query = request.GET.get('query', '').strip() # 2
    print('Query: {!r}'.format(query)) # 3
    if query: # 4
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**vars(descr)) for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'
        
    html = template.format(query=query, result=res, message=msg) # 5
    
    print('Sending {} results'.format(len(descriptions))) # 6
    return web.Response(content_type=CONTENT_TYPE, text=html) # 7

@asyncio.coroutine
def init(loop, address, port): # 1
    app = web.Application(loop=loop) #2
    app.router.add_route('GET', '/', home) #3
    handler = app.make_handler() # 4
    server = yield from loop.create_server(handler, address, port) # 5
    return server.sockets[0].getsockname() # 6


def main(address='127.0.0.1', port=8889):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port)) # 7
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever() # 8
    except KeyboardInterrupt: # 按CTRL-C键
        pass
    print('Server shutting down.')
    loop.close() # 9
    

if __name__ == '__main__':
    main(*sys.argv[1:])