#!/usr/bin/python3
'''
A simple Flask web application that displays a welcome message.
'''


from flask import Flask

# Initialize a new Flask web application instance
web_application = Flask(__name__)


@web_application.route('/', strict_slashes=False)
def home():
    '''
    Route handler for the root URL.

    Return a welcome message 'Hello HBNB' when the root URL is accessed.
    '''
    welcome_message = 'Hello HBNB!'
    return welcome_message


@web_application.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Route handler for the '/hbnb' URL.

    Returns the message 'HBNB' when the '/hbnb' URL is accessed.
    '''
    hbnb_message = 'HBNB'
    return hbnb_message


if __name__ == '__main__':
    # Run the web application on host 0.0.0.0 and port 500
    web_application.run(host='0.0.0.0', port=5000)
