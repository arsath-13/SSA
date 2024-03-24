from ..product import Product

class Battery(Product):
    def __init__(self, itemId, itemName, segment, district, month, year, sales_value, sales_quantity):
        super.__init__(itemId, itemName, segment, district, month, year, sales_value, sales_quantity)


