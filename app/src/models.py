from sqlalchemy import Column, Float, String, Integer
from database import Base

class Food(Base):
    __tablename__ = 'food_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    calories = Column(Float)
    carbohydrates = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    price = Column(Float)
    measure = Column(Float, nullable=False, default=100)
    unit = Column(String, nullable=False, default='g')

    def __init__(self, measure=None, unit=None, name=None, calories=None, carbohydrates=None, fat=None, protein=None, price=None):
        self.measure = measure
        self.unit = unit
        self.name = name
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.protein = protein
        self.price = price

    def __repr__(self):
        return 'food item ({} {}):\n  {}\n  Cal: {}\n  Carb: {}\n  Fat: {}\n  Prot: {}\n  $: {}\n'.format(
                self.measure,
                self.unit,
                self.name,
                self.calories,
                self.carbohydrates,
                self.fat,
                self.protein,
                self.price
                )
