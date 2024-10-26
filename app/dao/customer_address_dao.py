from .general_dao import GeneralDAO
from ..domain import CustomerAddress


class CustomerAddressDAO(GeneralDAO):
    _domain_type = CustomerAddress
