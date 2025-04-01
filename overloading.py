class one:
    def sum(self, a, b):
        print(a+b)

class two(one):
    def sum(self, a, b, c):
        print(a+b+c)




obj1 = one()
obj2 = two()

obj1.sum(10, 20, 20)
obj2.sum(10, 20, 30)

