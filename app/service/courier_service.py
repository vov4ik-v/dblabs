from .general_service import GeneralService
from ..dao import courier_dao


class CourierService(GeneralService):
    _dao = courier_dao
