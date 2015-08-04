from bottle import route, run
from bottle import template
from bottle import get, post, request # or route
from bottle import static_file
from bottle import response
from bottle import error

def f(x):
    return {
        'a': 1,
        'b': 2,
        }.get(x, 9) 

@route('/')
def server_static():
    return static_file('index.html', root='./')

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./')

@route('/msg/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@route('/hw')
def hello():
	return "Hello World!"

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

#passing static files (no paths)
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

#passing static files (with paths)
#@route('/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root='./')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/hw_cookie')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

run(host='localhost', port=8080, debug=True)
