from os import sys

import datetime
from database import db_session
from flask import Flask, request
from flask_cors import CORS
from models import Food, Meal

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'What\'s good?'


# Endpoint to save new food
@app.route('/api/savefood', methods=['GET', 'POST', 'OPTIONS'])
def save_food():
    if request.method == 'POST':
        try:
            data = request.get_json()
            app.logger.info('Received data: ' + str(data))
            food = Food(**data)
            db_session.add(food)
            db_session.commit()
        except Exception as ex:
            app.logger.info(ex)
            return 'Error saving food'
        return 'Food Saved'
    else:
        return 'GET'

# Endpoint to save new meal
@app.route('/api/savemeal', methods=['GET', 'POST', 'OPTIONS'])
def save_meal():
        if request.method == 'POST':
            try:
                data = request.get_json()
                app.logger.info('savemeal data: ' + str(data))
                date = datetime.date.today()
                meal = Meal('breakfast', date, 100, 100, 100, 10)
                db_session.add(meal)
                db_session.commit()
            except Exception as ex:
                app.logger.info(ex)
                return 'Error saving meal'
            return 'Meal Saved'
        else:
            return 'GET'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
