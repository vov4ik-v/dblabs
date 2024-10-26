from .general_service import GeneralService
from ..dao import customer_address_dao


class CustomerAddressService(GeneralService):
    _dao = customer_address_dao
