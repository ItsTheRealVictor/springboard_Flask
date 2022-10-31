from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'the main page for the Flask calculator exercise'




if __name__ == '__main__':
    app.run(debug=True)