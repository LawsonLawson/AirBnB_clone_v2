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


@web_application.route('/c/<text>', strict_slashes=False)
def display_custom_message(text):
    '''
    Route handler for the '/c/<text>' URL.

    Replaces underscores in the <input_text> parameter with spaces and
    returns a message formatted as 'C <formatted_text>'.

    Args:
    text (str): The text parameter provided in the URL, with underscores
    as separators.

    Returns:
    str: A formatted message 'C <formatted_text>'.
    '''
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


@web_application.route('/python', defaults={'text': 'is_cool'},
                       strict_slashes=False)
@web_application.route('/python/<text>', strict_slashes=False)
def display_python_message(text):
    '''
    Route handler for the '/python' and '/python/<custom_text>' URLs.

    Replaces underscores in the <custom_text> parameter with spaces and
    returns a message formatted as 'Python <formatted_text>'.
    If no custom text is provided, defaults to 'is_cool'.

    Args:
    text (str): The text parameter provided in the URL, with underscores as
    separators.

    Returns:
    str: A formatted message 'Python <formatted_text>'.
    '''
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)


if __name__ == '__main__':
    # Run the web application on host 0.0.0.0 and port 500
    web_application.run(host='0.0.0.0', port=5000)
