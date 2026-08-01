from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        # use of super() here so we dont need to go through the character class
        # actually call the constructor of the parent class.
        # this is mandatory because we override __init__
        super().__init__(first_name, is_alive)
        # proper constructor of the Baratheon class
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def die(self):
        """Set the character state to dead."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def die(self):
        """Set the character state to dead."""
        self.is_alive = False

    # use of cls -> the current class instead of the object itself
    # so effectively : cls(first_name, is_alive) is Lannister("Jaine", True)
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
