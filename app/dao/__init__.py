from .addon_dao import AddonDAO
from .courier_dao import CourierDAO
from .customer_dao import CustomerDAO
from .customer_address_dao import CustomerAddressDAO
from .cancelled_order_dao import CancelledOrderDAO
from .customer_feedback_dao import CustomerFeedbackDAO
from .delivery_dao import DeliveryDAO
from .product_dao import ProductDAO
from .ingredient_dao import IngredientDAO
from .order_detail_dao import OrderDetailDAO
from .order_dao import OrderDAO



addon_dao = AddonDAO()
courier_dao = CourierDAO()
customer_dao = CustomerDAO()
customer_address_dao = CustomerAddressDAO()
cancelled_order_dao = CancelledOrderDAO()
delivery_dao = DeliveryDAO()
product_dao = ProductDAO()
ingredient_dao = IngredientDAO()
order_detail_dao = OrderDetailDAO()
order_dao = OrderDAO()
customer_feedback = CustomerFeedbackDAO()