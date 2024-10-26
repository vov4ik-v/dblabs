from .order_service import OrderService
from .addon_service import AddonService
from .courier_service import CourierService
from .customer_service import CustomerService
from .customer_address_service import CustomerAddressService
from .cancelled_order_service import CancelledOrderService
from .delivery_service import DeliveryService
from .product_service import ProductService
from .ingredient_service import IngredientService
from .order_detail_service import OrderDetailService


addon_service = AddonService()
courier_service = CourierService()
customer_service = CustomerService()
customer_address_service = CustomerAddressService()
cancelled_order_service = CancelledOrderService()
delivery_service = DeliveryService()
product_service = ProductService()
ingredient_service = IngredientService()
order_detail_service = OrderDetailService()
order_service = OrderService()
