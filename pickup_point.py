class PickupPoint:

    def __init__(self, pickup_id=0, location="", status="", capacity=0, restocked=""):
        self._pickup_id = pickup_id
        self._location = location
        self._status = status
        self._capacity = capacity
        self._restocked = restocked

    def get_pickup_id(self):
        return self._pickup_id

    def get_location(self):
        return self._location

    def get_status(self):
        return self._status

    def get_capacity(self):
        return self._capacity

    def get_restocked(self):
        return self._restocked

    def set_pickup_id(self, pickup_id):
        self._pickup_id = pickup_id

    def set_location(self, location):
        self._location = location

    def set_status(self, status):
        self._status = status

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_restocked(self, restocked):
        self._restocked = restocked

    def to_file(self):
        return f"{self._pickup_id}#{self._location}#{self._status}#{self._capacity}#{self._restocked}"

    def __str__(self):
        return f"{self._pickup_id:<5}{self._location:<28}{self._status:<10}{self._capacity:<10}{self._restocked}"
