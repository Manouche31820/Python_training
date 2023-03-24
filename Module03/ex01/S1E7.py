from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

#your code here
    def die(self):
    	self.is_alive = False

    def __str__(self):
        pass

    def __repr__(self):
        return "Vector : 'Baratheon', 'brown', 'dark'"

class Lannister(Character):
    def __init__(self, first_name, boo : bool=True):
        self.first_name = first_name
        self.family_name = "Lannister"
        self.is_alive = boo
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        pass

    def __repr__(self):
        return "Vector : 'Lannister', 'blue', 'light'"

    def die(self):
    	self.is_alive = False

    def create_lannister(string : str, boo : bool=True):
    	return Lannister(string, boo)

if __name__ == '__main__':

    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")