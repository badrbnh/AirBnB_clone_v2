#!/usr/bin/python3
""" Starts a Flask web application"""""

from flask import *
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list_id(id=None):
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    if id is not None:
        for state in sorted_states:
            if state.id == id:
                return render_template('9-states.html', state=state,
                                    cities=sorted_cities, id=True)
            else:
                return render_template('9-states.html', state=None, id=id)
    else:
        return render_template('9-states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    """ Makes the app run when called from the command line"""
    app.run(host='0.0.0.0', port=5000)
