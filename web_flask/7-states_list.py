#!/usr/bin/python3
from flask import *
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of states."""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
