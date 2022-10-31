from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def mainRoute():
    return 'Its the main page, bruh'

@app.route('/search')
def search():
    resultOne = request.args['fart']
    resultTwo = request.args['dudu']
    return f'''Search results are as follows: \n
    first result: {resultOne}
    second result: {resultTwo}'''


if __name__ == '__main__':
    app.run(debug=True)