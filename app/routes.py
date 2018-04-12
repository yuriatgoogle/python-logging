from app import app
import logging
import random
import string

@app.route('/')
@app.route('/index')
def index():
    # print random string to log
    randomString = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    logging.warn("random string - " + randomString)
    return "Hello, World!"