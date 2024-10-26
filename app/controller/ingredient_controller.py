from .general_controller import GeneralController
from ..service import ingredient_service


class IngredientController(GeneralController):
    _service = ingredient_service
