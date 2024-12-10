# assign data type class on type key #Ticket MIDP-313
CUSTOMER_SCHEMA = [
    {
        "name": "customer_id",
        "type": int,
        "required": True
    },
    {
        "name": "first_name",
        "type": str,
        "required": True
    },
    {
        "name": "last_name",
        "type": str,
        "required": True
    },
    {
        "name": "gender",
        "type": str,
        "values": ["M", "F", "U"],
        "required": True
    },
    {
        "name": "email",
        "type": str,
        "required": True
    },
    {
        "name": "membership_status",
        "type": str,
        "values": ["active", "inactive"],
        "required": True
    },
    {
        "name": "address",
        "type": str,
    },
    {
        "name": "phone_number",
        "type": str,
        "required": False
    },
    {
        "name": "date_of_birth",
        "type": str,
        "format": "%Y-%m-%d",
        "required": True
    },
    {
        "name": "job",
        "type": str,
    },
    {
        "name": "company",
        "type": str,
    },
    {
        "name": "city",
        "type": str,
    },
    {
        "name": "state",
        "type": str,
    },
    {
        "name": "country",
        "type": str,
    },
    {
        "name": "language",
        "type": str,
        "values": ["en-US", "es-ES", "fr-FR"],
        "required": True
    }
]

SALES_SCHEMA = [
    {
        'name': 'sale_id',
        'type': int,
        'required': True
    },
    {
        "name": "customer_id",
        "type": int,
        "required": True
    },
    {
        "name": "product_id",
        "type": str,
        "required": True
    },
    {
        "name": "quantity",
        "type": int,
        "required": True
    },
    {
        "name": "price_per_unit",
        "type": float,
        "required": True
    },
    {
        "name": "total_price",
        "type": float,
        "required": True
    },
    {
        "name": "sale_date",
        "type": str,
        "format": "%Y-%m-%d",
        "required": True
    }
]

PRODUCT_SCHEMA = [
    {
        "name": "name",
        "type": str,
        "required": True
    },
    {
        "name": "product_id",
        "type": str,
        "required": True
    },
    {
        "name": "price",
        "type": float,
        "required": True
    },
    {
        "name": "description",
        "type": str,
    },
    {
        "name": "creation_date",
        "type": str,
        "format": "%Y-%m-%d",
        "required": True
    }
]
