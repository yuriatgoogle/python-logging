from flask import Flask
import logging
import random
import string
app = Flask(__name__)

@app.route('/')
def hello_world():
    # generate random 10-digit number to log
    randomString = ''.join([random.choice(string.digits) for n in xrange(10)])
    
    #randomly pick a logging level
    logLevel = random.randint(1,3)
    # logging.error("output value:" + randomString)
    
    # log based on level
    if (logLevel==1): 
        logging.error("myError:" + randomString)
        return "myError:" + randomString
    elif (logLevel==2): 
        logging.warn("myWarning:" + randomString)
        return "myWarning:" + randomString
    elif (logLevel==3):
        logging.debug("myDebugMessage:" + randomString)
        return "myDebug:" + randomString
    else:
        logging.fatal("problem")
        return "fatalError"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')