from bottle import run, route,  template


@route('/')
def home():
    return template('index')
 

run(debug = False, host='0.0.0.0', port=8080)
