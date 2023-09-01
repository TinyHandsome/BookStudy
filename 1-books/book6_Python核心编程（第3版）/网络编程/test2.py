from wsgiref.simple_server import make_server, demo_app

httpd = make_server('', 8080, demo_app)
print('Started app serving on port 8080')
httpd.serve_forever()