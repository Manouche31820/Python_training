from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name):
        '''Your docstring for Constructor'''
        self.first_name = first_name
        self.is_alive = True
    @abstractmethod
    def die(self):
        pass
class Stark(Character):
    """Your docstring for Cl"""
    def die(self):
    	'''Your docstring for Method'''
    	self.is_alive = False
