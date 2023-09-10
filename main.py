from bottle import run, route,  template


@route('/')
def home():
    return template('index')
 

run(debug = True, reloader = True)
