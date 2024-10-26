from .addon_controller import AddonController
from .courier_controller import CourierController
from .customer_controller import CustomerController
from .customer_address_controller import CustomerAddressController
from .cancelled_order_controller import CancelledOrderController
from .delivery_controller import DeliveryController
from .product_controller import ProductController
from .ingredient_controller import IngredientController
from .order_detail_controller import OrderDetailController
from .order_controller import OrderController


# Ініціалізація контролерів для додаткових таблиць
addon_controller = AddonController()
courier_controller = CourierController()
customer_controller = CustomerController()
customer_address_controller = CustomerAddressController()
cancelled_order_controller = CancelledOrderController()
delivery_controller = DeliveryController()
product_controller = ProductController()
ingredient_controller = IngredientController()
order_detail_controller = OrderDetailController()
order_controller = OrderController()
