class A:
    def __init__(self, a) -> None:
        self.a = a

    def printea(self):
        print(a)

    def get_a(self):
        return self.a


class B:
    def __init__(self, a) -> None:
        self.a = a

    def printea(self):
        print(a)

    def get_a(self):
        return self.a

lista = [1,2,3]
a = A(lista)
b = B(lista)

lista = [4,5,6]

print(lista)
a.printea()
b.printea()
print(hex(id(lista)) )
print(hex(id(a.get_a())))
print(hex(id(lista)) == hex(id(a.get_a())))