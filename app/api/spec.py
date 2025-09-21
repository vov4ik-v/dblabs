# app/api/spec.py
# Centralized Swagger/OpenAPI (Flasgger, Swagger 2.0)

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Restaurant Delivery API",
        "description": "Interactive Swagger UI to browse and execute API operations.",
        "version": "1.0.0",
    },
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "definitions": {
        # ===== Shared =====
        "Message": {
            "type": "object",
            "properties": {
                "message": {"type": "string", "example": "OK"}
            }
        },

        # ===== Addon =====
        "Addon": {
            "type": "object",
            "properties": {
                "addon_id": {"type": "integer", "example": 1},
                "name": {"type": "string", "example": "Extra cheese"},
                "price": {"type": "number", "format": "float", "example": 1.99}
            },
            "required": ["name", "price"]
        },
        "AddonCreate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "Chili sauce"},
                "price": {"type": "number", "format": "float", "example": 0.5}
            },
            "required": ["name", "price"]
        },
        "AddonUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "Updated name"},
                "price": {"type": "number", "format": "float", "example": 2.49}
            }
        },

        # ===== CancelledOrder =====
        "CancelledOrder": {
            "type": "object",
            "properties": {
                "cancelled_order_id": {"type": "integer", "example": 10},
                "order_id": {"type": "integer", "example": 123},
                "reason": {"type": "string", "example": "Customer not at home"},
                "comment": {"type": "string", "example": "Tried to call twice"},
                "created_at": {"type": "string", "example": "2025-09-01T12:00:00Z"}
            },
            "required": ["order_id", "reason"]
        },
        "CancelledOrderCreate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer", "example": 123},
                "reason": {"type": "string", "example": "Customer not at home"},
                "comment": {"type": "string", "example": "Tried to call twice"}
            },
            "required": ["order_id", "reason"]
        },
        "CancelledOrderUpdate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer"},
                "reason": {"type": "string"},
                "comment": {"type": "string"}
            }
        },

        # ===== Courier =====
        "Courier": {
            "type": "object",
            "properties": {
                "courier_id": {"type": "integer", "example": 1},
                "name": {"type": "string", "example": "Alex Rider"},
                "phone": {"type": "string", "example": "+380501112233"},
                "active": {"type": "boolean", "example": True}
            },
            "required": ["name", "phone"]
        },
        "CourierCreate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "Alex Rider"},
                "phone": {"type": "string", "example": "+380501112233"}
            },
            "required": ["name", "phone"]
        },
        "CourierUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "phone": {"type": "string"},
                "active": {"type": "boolean"}
            }
        },

        # ===== CustomerAddress =====
        "CustomerAddress": {
            "type": "object",
            "properties": {
                "address_id": {"type": "integer", "example": 5},
                "customer_id": {"type": "integer", "example": 1},
                "address": {"type": "string", "example": "1 High St, London"},
                "city": {"type": "string", "example": "Kyiv"},
                "postal_code": {"type": "string", "example": "01001"}
            },
            "required": ["customer_id", "address"]
        },
        "CustomerAddressCreate": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer", "example": 1},
                "address": {"type": "string", "example": "1 High St, London"},
                "city": {"type": "string", "example": "Kyiv"},
                "postal_code": {"type": "string", "example": "01001"}
            },
            "required": ["customer_id", "address"]
        },
        "CustomerAddressUpdate": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer"},
                "address": {"type": "string"},
                "city": {"type": "string"},
                "postal_code": {"type": "string"}
            }
        },

        # ===== Customer =====
        "Customer": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer", "example": 1},
                "name": {"type": "string", "example": "John Doe"},
                "email": {"type": "string", "example": "john@example.com"},
                "phone": {"type": "string", "example": "+380501112233"},
                "addresses": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/CustomerAddress"}
                }
            },
            "required": ["name", "email"]
        },
        "CustomerCreate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "John Doe"},
                "email": {"type": "string", "example": "john@example.com"},
                "phone": {"type": "string", "example": "+380501112233"}
            },
            "required": ["name", "email"]
        },
        "CustomerUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"}
            }
        },

        # ===== Delivery =====
        "Delivery": {
            "type": "object",
            "properties": {
                "delivery_id": {"type": "integer", "example": 7},
                "order_id": {"type": "integer", "example": 123},
                "courier_id": {"type": "integer", "example": 1},
                "status": {"type": "string", "example": "in_progress"},
                "delivered_at": {"type": "string", "example": "2025-09-01T14:00:00Z"}
            }
        },
        "DeliveryCreate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer"},
                "courier_id": {"type": "integer"},
                "status": {"type": "string", "example": "pending"}
            },
            "required": ["order_id", "courier_id"]
        },
        "DeliveryUpdate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer"},
                "courier_id": {"type": "integer"},
                "status": {"type": "string"},
                "delivered_at": {"type": "string"}
            }
        },

        # ===== Ingredient =====
        "Ingredient": {
            "type": "object",
            "properties": {
                "ingredient_id": {"type": "integer", "example": 3},
                "name": {"type": "string", "example": "Tomato"}
            },
            "required": ["name"]
        },
        "IngredientCreate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "Tomato"}
            },
            "required": ["name"]
        },
        "IngredientUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        },

        # ===== OrderDetail =====
        "OrderDetail": {
            "type": "object",
            "properties": {
                "order_detail_id": {"type": "integer", "example": 55},
                "order_id": {"type": "integer", "example": 123},
                "product_id": {"type": "integer", "example": 101},
                "quantity": {"type": "integer", "example": 2},
                "addon_id": {"type": "integer", "example": 1}
            }
        },
        "OrderDetailCreate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer", "example": 123},
                "product_id": {"type": "integer", "example": 101},
                "quantity": {"type": "integer", "example": 2},
                "addon_id": {"type": "integer", "example": 1}
            },
            "required": ["order_id", "product_id", "quantity"]
        },
        "OrderDetailUpdate": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer"},
                "product_id": {"type": "integer"},
                "quantity": {"type": "integer"},
                "addon_id": {"type": "integer"}
            }
        },

        # ===== Order =====
        "Order": {
            "type": "object",
            "properties": {
                "order_id": {"type": "integer", "example": 123},
                "customer_id": {"type": "integer", "example": 1},
                "delivery_address_id": {"type": "integer", "example": 5},
                "comment": {"type": "string", "example": "Ring the doorbell"},
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "product_id": {"type": "integer", "example": 101},
                            "quantity": {"type": "integer", "example": 2}
                        }
                    }
                }
            }
        },
        "OrderCreate": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer", "example": 1},
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "product_id": {"type": "integer", "example": 101},
                            "quantity": {"type": "integer", "example": 2}
                        }
                    }
                },
                "delivery_address_id": {"type": "integer", "example": 5},
                "comment": {"type": "string", "example": "Ring the doorbell"}
            },
            "required": ["customer_id", "items"]
        },
        "OrderUpdate": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer"},
                "items": {"type": "array", "items": {"type": "object"}},
                "delivery_address_id": {"type": "integer"},
                "comment": {"type": "string"}
            }
        },

        # ===== Product =====
        "Product": {
            "type": "object",
            "properties": {
                "product_id": {"type": "integer", "example": 101},
                "name": {"type": "string", "example": "Pizza Margherita"},
                "price": {"type": "number", "format": "float", "example": 12.5},
                "ingredient_ids": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "example": [1, 2, 3]
                }
            },
            "required": ["name", "price"]
        },
        "ProductCreate": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "example": "Pizza Margherita"},
                "price": {"type": "number", "format": "float", "example": 12.5},
                "ingredient_ids": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "example": [1, 2, 3]
                }
            },
            "required": ["name", "price"]
        },
        "ProductUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number", "format": "float"},
                "ingredient_ids": {
                    "type": "array",
                    "items": {"type": "integer"}
                }
            }
        }
    }
}
