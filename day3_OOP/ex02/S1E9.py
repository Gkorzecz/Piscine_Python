from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""

    # constructor of the class, =True says that is_alive is optionnaly defined
    def __init__(self, first_name, is_alive=True):
        """Construct the object with two attributes, initiated with argument"""
        # create the attributes of the object
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to change the character state to dead"""
        # pass is mandatory because every function must have something inside
        pass


class Stark(Character):
    """Class representing a Stark character"""

    # every subclass must define the function die.
    def die(self):
        """Set the character state to dead"""
        self.is_alive = False
