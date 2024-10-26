from .general_dao import GeneralDAO
from ..domain import Addon


class AddonDAO(GeneralDAO):
    _domain_type = Addon
