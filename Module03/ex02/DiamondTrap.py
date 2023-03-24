from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):

    def __init__(self, first_name):
        super().__init__(first_name)

    def set_eyes(self, string:str):
        self.eyes = string

    def set_hairs(self, string:str):
        self.hairs = string

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
