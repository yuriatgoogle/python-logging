from flask import Flask
import logging
import random
import string
app = Flask(__name__)

@app.route('/')
def hello_world():
    # generate random string to log
    randomString = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    
    #randomly pick a logging level
    logLevel = random.randint(1,3)
    logging.info("log level is " + str(logLevel))
    
    # log based on level
    if (logLevel==1): 
        logging.error("random string:" + randomString)
    elif (logLevel==2): 
        logging.warn("random string:" + randomString)
    elif (logLevel==3):
        logging.debug("random string:" + randomString)
    else:
        logging.fatal("problem")
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')