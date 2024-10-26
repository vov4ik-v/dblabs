from .general_controller import GeneralController
from ..service import customer_address_service


class CustomerAddressController(GeneralController):
    _service = customer_address_service
