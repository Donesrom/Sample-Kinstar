from bottle import run, route,  template


@route('/')
def home():
    return template('index')
 

run()


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
