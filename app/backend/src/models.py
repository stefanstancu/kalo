from sqlalchemy import Column, Float, String, Integer, Date
from database import Base

class Food(Base):
    __tablename__ = 'food_items'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    calories = Column(Float)
    carbohydrates = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    price = Column(Float)
    measure = Column(Float, nullable=False, default=100)
    unit = Column(String, nullable=False, default='g')

    def __init__(self, measure=None, unit=None, name=None, user_id=None, calories=None, carbohydrates=None, fat=None, protein=None, price=None):
        self.measure = measure
        self.unit = unit
        self.name = name
        self.user_id = user_id
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.protein = protein
        self.price = price

    def __repr__(self):
        return 'food item ({} {}):\n  {}\n  {}\n Cal: {}\n  Carb: {}\n  Fat: {}\n  Prot: {}\n  $: {}\n'.format(
                self.measure,
                self.unit,
                self.name,
                self.user_id,
                self.calories,
                self.carbohydrates,
                self.fat,
                self.protein,
                self.price
                )
    @property
    def serialize(self):
        """Return a dict of the object for returning to front-end"""
        return {
                'id': self.id,
                'name': self.name,
                'measure': self.measure,
                'calories': self.calories,
                'carbohydrates': self.carbohydrates,
                'fat': self.fat,
                'protein': self.protein,
                'price': self.price
                }

    def __name__(self):
        return self.name

class Meal(Base):
    __tablename__ = 'meal_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    calories = Column(Float)
    carbohydrates = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    price = Column(Float)

    def __init__(self, name, user_id, date, calories, carbohydrates, fat, protein, price=0):
        self.name = name
        self.user_id = user_id
        self.date = date
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.protein = protein
        self.price = price

    def __repr__(self):
        return 'user: {}\n meal ({}, {}):\n Cal: {}\n  Carb: {}\n  Fat: {}\n  Prot: {}\n  $: {}\n'.format(
                self.user_id,
                self.name,
                self.date,
                self.calories,
                self.carbohydrates,
                self.fat,
                self.protein,
                self.price
                )

    @property
    def serialize(self):
        """Return a dict of the object for returning to front-end"""
        return {
                'id': self.id,
                'name': self.name,
                'date': str(self.date),
                'calories': self.calories,
                'carbohydrates': self.carbohydrates,
                'fat': self.fat,
                'protein': self.protein,
                'price': self.price
                }

class Weight(Base):
    __tablename__ = 'weight'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_id = Column(String, nullable=False)
    kg = Column(Float)
    lbs = Column(Float)

    def __init__(self, user_id, date, kg, lbs):
        self.date = date
        self.kg = kg
        self.lbs = lbs
        self.user_id = user_id

    def __repr__(self):
        return 'user: {}\n date:{}\n kg: {}\n lbs: {}\n'.format(
                self.user_id,
                self.date,
                self.kg,
                self.lbs
                )
    @property
    def serialize(self):
        """Return a dict of the object for returning to front-end"""
        return {
                'date': self.date,
                'kg': self.kg,
                'lbs': self.lbs
                }

