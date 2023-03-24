class calculator:

    def __init__(self, liste):
        self.liste = liste

    def __add__(self, object) -> None:
        for i in range(len(self.liste)):
            self.liste[i] += object
        print(self.liste)

    def __mul__(self, object) -> None:

        for i in range(len(self.liste)):
            self.liste[i] *= object
        print(self.liste)

    def __sub__(self, object) -> None:

        for i in range(len(self.liste)):
            self.liste[i] -= object
        print(self.liste)
    def __truediv__(self, object) -> None:

        for i in range(len(self.liste)):
            self.liste[i] /= object
        print(self.liste)
