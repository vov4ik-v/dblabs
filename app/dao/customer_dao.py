from .general_dao import GeneralDAO
from ..domain import Customer


class CustomerDAO(GeneralDAO):
    _domain_type = Customer
