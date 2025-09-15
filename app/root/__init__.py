from flask import Flask

from .customer_feedback_route import customer_feedback_bp
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .addon_route import addon_bp
    from .courier_route import courier_bp
    from .customer_route import customer_bp
    from .customer_address_route import customer_address_bp
    from .cancelled_order_route import cancelled_order_bp
    from .delivery_route import delivery_bp
    from .product_route import product_bp
    from .ingredient_route import ingredient_bp
    from .order_detail_route import order_detail_bp
    from .order_route import order_bp

    app.register_blueprint(addon_bp)
    app.register_blueprint(courier_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(customer_address_bp)
    app.register_blueprint(cancelled_order_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(ingredient_bp)
    app.register_blueprint(order_detail_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(customer_feedback_bp)
