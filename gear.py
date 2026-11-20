class Gear:

    def __init__(self, gear_id=0, item="", gear_type="", rate=0.0, status="", pickup_id=0, total_units=0, units_available=0):
        self._gear_id = gear_id
        self._item = item
        self._gear_type = gear_type
        self._rate = rate
        self._status = status
        self._pickup_id = pickup_id
        self._total_units = total_units
        self._units_available = units_available

    def get_gear_id(self):
        return self._gear_id

    def get_item(self):
        return self._item

    def get_gear_type(self):
        return self._gear_type

    def get_rate(self):
        return self._rate

    def get_status(self):
        return self._status

    def get_pickup_id(self):
        return self._pickup_id

    def get_total_units(self):
        return self._total_units

    def get_units_available(self):
        return self._units_available

    def set_gear_id(self, gear_id):
        self._gear_id = gear_id

    def set_item(self, item):
        self._item = item

    def set_gear_type(self, gear_type):
        self._gear_type = gear_type

    def set_rate(self, rate):
        self._rate = rate

    def set_status(self, status):
        self._status = status

    def set_pickup_id(self, pickup_id):
        self._pickup_id = pickup_id

    def set_total_units(self, total_units):
        self._total_units = total_units

    def set_units_available(self, units_available):
        self._units_available = units_available

    def to_file(self):
        return f"{self._gear_id}#{self._item}#{self._gear_type}#{self._rate:.2f}#{self._status}#{self._pickup_id}#{self._total_units}#{self._units_available}"

    def __str__(self):
        return f"{self._gear_id:<5}{self._item:<30}{self._gear_type:<10}${self._rate:<8.2f}{self._status:<13}{self._pickup_id:<8}{self._units_available}/{self._total_units}"
