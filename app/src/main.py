from os import sys
from flask import Flask, request
from database import db_session
from models import Food

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'What\'s good?'

# Endpoint to save new food
@app.route('/api/savefood', methods=['GET', 'POST'])
def save_food():
    if request.method == 'POST':
        data = request.get_json()
        print(data, file=sys.stderr)
        food = Food(**data)
        db_session.add(food)
        db_session.commit()
        return 'Food Saved'

    else:
        return 'GET'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
