from .general_service import GeneralService
from ..dao import customer_dao


class CustomerService(GeneralService):
    _dao = customer_dao
