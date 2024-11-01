from .general_controller import GeneralController
from ..domain.product import Product
from ..service import product_service


class ProductController(GeneralController):
    _service = product_service

    def find_all_products_with_ingredients(self):
        # Fetch all products with ingredients eagerly loaded
        return self.find_all(Product.ingredients)

    def find_product_with_ingredients(self, product_id: int):
        # Fetch a single product with ingredients eagerly loaded
        return self.find_by_id(product_id, Product.ingredients)
