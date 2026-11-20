class Rental:

    def __init__(self, rental_id=0, email="", gear_id=0, pickup_id=0, date="", start="", end="N/A", cost="N/A", status=""):
        self._rental_id = rental_id
        self._email = email
        self._gear_id = gear_id
        self._pickup_id = pickup_id
        self._date = date
        self._start = start
        self._end = end
        self._cost = cost
        self._status = status

    def get_rental_id(self):
        return self._rental_id

    def get_email(self):
        return self._email

    def get_gear_id(self):
        return self._gear_id

    def get_pickup_id(self):
        return self._pickup_id

    def get_date(self):
        return self._date

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_cost(self):
        return self._cost

    def get_status(self):
        return self._status

    def set_rental_id(self, rental_id):
        self._rental_id = rental_id

    def set_email(self, email):
        self._email = email

    def set_gear_id(self, gear_id):
        self._gear_id = gear_id

    def set_pickup_id(self, pickup_id):
        self._pickup_id = pickup_id

    def set_date(self, date):
        self._date = date

    def set_start(self, start):
        self._start = start

    def set_end(self, end):
        self._end = end

    def set_cost(self, cost):
        self._cost = cost

    def set_status(self, status):
        self._status = status

    def to_file(self):
        return f"{self._rental_id}#{self._email}#{self._gear_id}#{self._pickup_id}#{self._date}#{self._start}#{self._end}#{self._cost}#{self._status}"

    def __str__(self):
        return f"{self._rental_id:<5}{self._email:<25}{self._gear_id:<6}{self._pickup_id:<8}{self._date:<12}{self._start:<7}{self._end:<7}{self._cost:<8}{self._status}"
