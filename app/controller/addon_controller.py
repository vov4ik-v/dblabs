from .general_controller import GeneralController
from ..service import addon_service


class AddonController(GeneralController):
    _service = addon_service
