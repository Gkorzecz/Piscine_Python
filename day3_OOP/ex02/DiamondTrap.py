from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # we SHOULD use __dict__ because 'self.eyes = value' would call set_eyes
    # and cause an infinit recursion,
    def get_eyes(self):
        return self.__dict__["eyes"]

    def set_eyes(self, value):
        self.__dict__["eyes"] = value

    def get_hairs(self):
        return self.__dict__["hairs"]

    def set_hairs(self, value):
        self.__dict__["hairs"] = value

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)
