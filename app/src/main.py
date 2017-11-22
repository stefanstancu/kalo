from os import sys
from flask import Flask, request
from database import db_session
from models import Food
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'What\'s good?'

# Endpoint to save new food
@app.route('/api/savefood', methods=['GET', 'POST','OPTIONS'])
def save_food():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data, file=sys.stderr)
            food = Food(**data)
            db_session.add(food)
            db_session.commit()
        except Exception:
            return 'Error saving food'
        return 'Food Saved'
    else:
        return 'GET'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

