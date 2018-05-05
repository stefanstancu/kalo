import datetime
import json

from meal import food_to_meal

from os import sys
from database import db_session
from flask import Flask, request, session
from flask_cors import CORS
from models import Food, Meal

import auth

app = Flask(__name__)
app.secret_key = 'test'
CORS(app, supports_credentials=True)

# Endpoint to save new food
@app.route('/api/savefood', methods=['GET', 'POST', 'OPTIONS'])
def save_food():
    if request.method == 'POST':
        try:
            data = request.get_json()

            if 'token' in session:
                token = session['token']
                user_id = auth.validate_user(token)
            else:
                return "Please sign in"

            app.logger.info('Received data: ' + str(data))
            food = Food(**data)
            food.user_id = user_id
            db_session.add(food)
            db_session.commit()
        except Exception as ex:
            app.logger.error(ex)
            return 'Error saving food'
        return 'Food Saved'
    else:
        return '-'

# Endpoint to save new meal
@app.route('/api/savemeal', methods=['GET', 'POST', 'OPTIONS'])
def save_meal():
        if request.method == 'POST':
            try:
                data = request.get_json()
                if 'token' in session:
                    token = session['token']
                    user_id = auth.validate_user(token)
                else:
                    return "Please sign in"

                app.logger.debug('savemeal data: ' + str(data))
                meal = food_to_meal(data['name'], user_id, data['items'], app) 
                if isinstance(meal, str):
                    return meal

                meal.user_id = user_id
                db_session.add(meal)
                db_session.commit()
            except Exception as ex:
                app.logger.error(ex)
                return 'Error saving meal'
            return 'Meal Saved'
        else:
            return '-'

# Endpoint to request meals eaten in a specific day
@app.route('/api/getmeals', methods=['GET','POST', 'OPTIONS'])
def get_meals():
    if request.method == 'POST':
        try:
            data = request.get_json()

            if 'token' in session:
                token = session['token']
                user_id = auth.validate_user(token)
            else:
                return "Please sign in"

            app.logger.info('getmeal request: ' + str(data))
            meals = db_session.query(Meal).\
                    filter(Meal.date==datetime.date.today()).\
                    filter(Meal.user_id == user_id).\
                    all()
            meals = json.dumps([i.serialize for i in meals])
            app.logger.info(meals)
        except Exception as ex:
            app.logger.error(ex)
            return 'Error getting meals'
        return meals
    else:
        return 'success'

# Endpoint to request foods that have been saved by the user
@app.route('/api/getfoods', methods=['GET','POST', 'OPTIONS'])
def get_foods():
    if request.method == 'POST':
        try:
            app.logger.info('getfood request')

            if 'token' in session:
                token = session['token']
                user_id = auth.validate_user(token)
            else:
                return "Please sign in"

            foods = db_session.query(Food).filter(Food.user_id == user_id).all()
            foods = json.dumps([i.serialize for i in foods])
            app.logger.info(foods)
        except Exception as ex:
            app.logger.error(ex)
            return 'Error getting foods'
        return foods
    else:
        return 'success'

# Login endpoint
@app.route('/api/login', methods=['GET', 'POST', 'OPTIONS'])
def login():
    if request.method == 'POST':
        try:
            app.logger.info('login attempt')
            data = request.get_json()

            user_id = auth.validate_user(data['token'])
            session['token'] = data['token']

        except Exception as ex:
            app.logger.error(ex)
            return 'Error loggging in'
        app.logger.info('user logged in ' + user_id)
        return 'login successuful'
    else:
        return 'success'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
