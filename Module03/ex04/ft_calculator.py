class calculator:

    def __init__(self, liste1, liste2):
        self.liste1 = liste1
        self.liste2 = liste2

    def copy(self, V1: list[float]):
        copy_V1 = V1.copy(V1)
        return copy_V1

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        k = 0
        V3 = V1.copy()
        for i in range(len(V1)):
            V3[i] = V1[i] * V2[i]
        for i in V3:
            k += i       
        print("Dot product is : ", k)

    def add_vec(V1: list[float], V2: list[float]) -> None:

        V3 = V1.copy()
        for i in range(len(V1)):
            V3[i] = float(V2[i]) + float(V1[i])
        print("Add vector is :", V3)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        V3 = V1.copy()
        for i in range(len(V1)):
            V3[i] = float(V1[i]) - float(V2[i])
        print("Sous vector is :", V3)
    

# if __name__ == '__main__':
#     a = [5, 10, 2]
#     b = [2, 4, 3]
#     calculator.dotproduct(a,b)
#     calculator.add_vec(a,b)
#     calculator.sous_vec(a,b)
