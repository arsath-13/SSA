class Battery:
    def __init__(self, itemId, itemName, segment):
        self._itemId = itemId
        self._itemName = itemName
        self._segment = segment

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
