#!/usr/bin/python3
'''
Flask Web Application

This script starts a Flask web application that displays a list of states from
a storage backend in alphabetical order
'''

# Import Flask and render_template from flask
from flask import Flask, render_template

# Import storage from models
from models import storage

# Import State model to reference it directly
from models.state import State

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
    Display a HTML page with the states listed in alphabetical order.

    Retrieves all State objects from the storage backend, sorts them by name,
    and renders an HTML template to display the sorted list of states.
    '''
    # Retrieve all State objects from storage and sort them by name
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)

    # Render the template '7-states_list.html' with the sorted states
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    '''
    Close the storage on teardown.

    This function is called after each request to ensure the storage is
    properly closed, which helps to release resources and maintain
    application performance.
    '''
    storage.close()


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
