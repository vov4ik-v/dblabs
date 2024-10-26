from .general_dao import GeneralDAO
from ..domain import Product


class ProductDAO(GeneralDAO):
    _domain_type = Product
