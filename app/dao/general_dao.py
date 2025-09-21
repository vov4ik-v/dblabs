from abc import ABC
from typing import List
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload, Mapper
from app import db

class GeneralDAO(ABC):
    _domain_type = None

    def find_all(self, *relations) -> List[object]:
        with db.session() as session:
            query = session.query(self._domain_type)
            for relation in relations:
                query = query.options(joinedload(relation))
            return query.all()

    def find_by_id_with_relations(self, key: int, *relations) -> object:
        with db.session() as session:
            query = session.query(self._domain_type)
            for relation in relations:
                query = query.options(joinedload(relation))
            return query.get(key)

    def create(self, obj: object) -> object:
        try:
            with db.session() as session:
                session.add(obj)
                session.commit()
                session.refresh(obj)
                return obj
        except SQLAlchemyError:
            session.rollback()
            raise

    def create_all(self, obj_list: List[object]) -> List[object]:
        with db.session() as session:
            session.add_all(obj_list)
            session.commit()
            return obj_list

    def update(self, key: int, in_obj: object) -> None:
        with db.session() as session:
            domain_obj = session.query(self._domain_type).get(key)
            mapper: Mapper = inspect(type(in_obj))
            columns = mapper.columns._collection
            for column_name, column_obj, *_ in columns:
                if not column_obj.primary_key:
                    value = getattr(in_obj, column_name)
                    setattr(domain_obj, column_name, value)
            session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        with db.session() as session:
            domain_obj = session.query(self._domain_type).get(key)
            setattr(domain_obj, field_name, value)
            session.commit()

    def delete(self, key: int) -> None:
        with db.session() as session:
            domain_obj = session.query(self._domain_type).get(key)
            session.delete(domain_obj)
            try:
                session.commit()
            except Exception:
                session.rollback()
                raise

    def delete_all(self) -> None:
        with db.session() as session:
            session.query(self._domain_type).delete()
            session.commit()
