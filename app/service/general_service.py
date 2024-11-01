from abc import ABC
from typing import List

class GeneralService(ABC):
    _dao = None

    def find_all(self, *relations) -> List[object]:
        return self._dao.find_all(*relations)

    def find_by_id_with_relations(self, key: int, *relations) -> object:
        return self._dao.find_by_id_with_relations(key, *relations)

    def create(self, obj: object) -> object:
        return self._dao.create(obj)

    def create_all(self, obj_list: List[object]) -> List[object]:
        return self._dao.create_all(obj_list)

    def update(self, key: int, obj: object) -> None:
        self._dao.update(key, obj)

    def patch(self, key: int, field_name: str, value: object) -> None:
        self._dao.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        self._dao.delete(key)

    def delete_all(self) -> None:
        self._dao.delete_all()
