class Customer:

    def __init__(self, email="", first_name="", last_name="", phone="", status=""):
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._status = status

    def get_email(self):
        return self._email

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_phone(self):
        return self._phone

    def get_status(self):
        return self._status

    def set_email(self, email):
        self._email = email

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_phone(self, phone):
        self._phone = phone

    def set_status(self, status):
        self._status = status

    def to_file(self):
        return f"{self._email}#{self._first_name}#{self._last_name}#{self._phone}#{self._status}"

    def __str__(self):
        name = self._first_name + " " + self._last_name
        return f"{self._email:<25}{name:<22}{self._phone:<15}{self._status}"
