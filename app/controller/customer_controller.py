from .general_controller import GeneralController
from ..service import customer_service


class CustomerController(GeneralController):
    _service = customer_service
