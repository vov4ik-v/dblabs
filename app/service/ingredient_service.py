from .general_service import GeneralService
from ..dao import ingredient_dao


class IngredientService(GeneralService):
    _dao = ingredient_dao
