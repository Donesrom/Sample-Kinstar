import os
import socketserver
import http.server
from bottle import run, route,  template


@route('/')
def home():
    return template('index')
 

run(host = '0.0.0.0')


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
