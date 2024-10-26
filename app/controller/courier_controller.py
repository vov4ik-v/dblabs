from .general_controller import GeneralController
from ..service import courier_service


class CourierController(GeneralController):
    _service = courier_service
