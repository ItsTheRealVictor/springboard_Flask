from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def mainRoute():
    return 'Its the main page, bruh'

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add a comment, bruh</h1>
    <form method='POST'>
    <input type='text' placeholder='Put a comment here, bruh' name='comment'/>
    <input type='text' placeholder='Whats your username?' name='username'/>
    <button>Submit</button>
    
    </form>
    """

@app.route('/add-comment', methods=['POST'])
def save_comment_form():

    userComment = request.form['comment']
    userName = request.form['username']

    print(request.form)
    return f"""
    <h1>This was your comment: {userComment}</h1>
    <h1>This was your username: {userName}</h1>

    
    
    """

farts = {
    1: 'NOOOOICE',
    2: 'Eggs for lunch',
    3: 'OMG farts',
    4: 'ayyyyyyyyyy'
}


@app.route('/r/<int:id>')
def show_subreddit(id):
    post = farts.get(id, 'nah did not find that shit')
    return f'your post is {post}'



if __name__ == '__main__':
    app.run(debug=True)