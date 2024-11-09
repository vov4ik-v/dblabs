from .general_dao import GeneralDAO
from ..domain import Courier


class CourierDAO(GeneralDAO):
    _domain_type = Courier

    def find_by_id(self, courier_id: int) -> Courier:
        return Courier.query.get(courier_id)

