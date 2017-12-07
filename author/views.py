from __init__ import app

@app.route('/login')
def login():
    return "Hello user!"