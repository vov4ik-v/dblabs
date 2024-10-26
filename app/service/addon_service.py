from .general_service import GeneralService
from ..dao import addon_dao


class AddonService(GeneralService):
    _dao = addon_dao
