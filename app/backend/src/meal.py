import datetime
from database import db_session
from models import Food, Meal

def food_to_meal(name, user_id, foods, date, app):
    """ Converts the food dictionary to a meal object to save in the db """
    
    foods = _build_food_dict(foods)
    app.logger.debug(foods)
    try:
        saved_food = db_session.query(Food).\
                filter(Food.user_id == user_id).\
                filter(Food.name.in_(foods.keys())).\
                all()
    except Exception as ex:
        app.logger.info(ex)
        return "error getting foods, has it been added?"

    meal = Meal(name, user_id, date, 0, 0, 0, 0)
    for item in saved_food:
        meal.calories += item.calories/item.measure*foods[item.name]
        meal.carbohydrates += item.carbohydrates/item.measure*foods[item.name]
        meal.fat += item.fat/item.measure*foods[item.name]
        meal.protein += item.protein/item.measure*foods[item.name]

    return meal

def _build_food_dict(foods):
    """ 
        Changes the format of the data for better readability during proccessing
        Goes from {name:"string", amount:int} to {string: int}
    """
    dct = {}
    for item in foods:
        dct[item['name']] = float(item['amount'])

    return dct
