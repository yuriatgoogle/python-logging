from app import app

@app.route('/')
@app.route('/index')
def index():
    // TODO - add logging
    return "Hello, World!"