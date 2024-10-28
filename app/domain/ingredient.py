from __future__ import annotations
from typing import Dict, Any
from app import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    weight_grams = db.Column(db.Float, nullable=False)

    product = db.relationship('Product', back_populates='ingredients')

    def __init__(self, name: str, product_id: int, weight_grams: float, ingredient_id: int = None):
        self.ingredient_id = ingredient_id
        self.name = name
        self.product_id = product_id
        self.weight_grams = weight_grams

    def __repr__(self) -> str:
        return f"Ingredient({self.ingredient_id}, '{self.name}', {self.product_id}, {self.weight_grams})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'ingredient_id': self.ingredient_id,
            'name': self.name,
            'product_id': self.product_id,
            'weight_grams': self.weight_grams
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ingredient:
        return Ingredient(
            ingredient_id=dto_dict.get('ingredient_id'),
            name=dto_dict.get('name'),
            product_id=dto_dict.get('product_id'),
            weight_grams=dto_dict.get('weight_grams')
        )
