from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'the main page for the Flask calculator exercise'

@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))

@app.route('/sub')
def subtraction():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))

@app.route('/mult')
def multiplication():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))

    
@app.route('/div')
def division():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))


operations = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations[operation](a,b))




if __name__ == '__main__':
    app.run(debug=True)