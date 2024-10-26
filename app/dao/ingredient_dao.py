from .general_dao import GeneralDAO
from ..domain import Ingredient


class IngredientDAO(GeneralDAO):
    _domain_type = Ingredient
