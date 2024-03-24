class Product:
    def __init__(self, itemId, itemName, segment, district, month, year, sales_value, sales_quantity):
        self._itemId = itemId
        self._itemName = itemName
        self._segment = segment
        self._district = district
        self._month = month
        self._year = year
        self._sales_value = sales_value
        self._sales_quantity = sales_quantity

    @property
    def itemId(self):
        return self._itemId

    @itemId.setter
    def itemId(self, value):
        self._itemId = value

    @property
    def itemName(self):
        return self._itemName

    @itemName.setter
    def itemName(self, value):
        self._itemName = value

    @property
    def segment(self):
        return self._segment

    @segment.setter
    def segment(self, value):
        self._segment = value

    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def sales_value(self):
        return self._sales_value

    @sales_value.setter
    def sales_value(self, value):
        self._sales_value = value

    @property
    def sales_quantity(self):
        return self._sales_quantity

    @sales_quantity.setter
    def sales_quantity(self, value):
        self._sales_quantity = value
