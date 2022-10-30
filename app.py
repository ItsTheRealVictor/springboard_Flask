from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainRoute():
    return 'Its the main page, bruh'



@app.route('/hello')
def say_hello():
    html = """
        <h1> FARTS </h1>
        <h2> FARTS </h2>
        <h3> FARTS </h3>
    """
    return html

@app.route('/later')
def say_later():
    return 'later bruh'

if __name__ == '__main__':
    app.run(debug=True)