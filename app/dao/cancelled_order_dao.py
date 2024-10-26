from .general_dao import GeneralDAO
from ..domain import CancelledOrder


class CancelledOrderDAO(GeneralDAO):
    _domain_type = CancelledOrder
