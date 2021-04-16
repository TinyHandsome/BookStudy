from wsgiref.simple_server import make_server

def simple_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return ['Hello World!']

httpd = make_server('', 8080, simple_wsgi_app)
print('Start app serving on port 8080...')
httpd.serve_forever()
