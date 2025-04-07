class Add:
    def add(self, a, b):
        return a+b

class Sub:
    def sub(self, a, b):
        return a - b

class Mul:
    def mul(self, a, b):
        return a * b

class derivedClass(Add, Sub, Mul):
    def div(self, a, b):
        return a / b


a, b = 10, 20
obj = derivedClass()
print(obj.add(a, b))
print(obj.sub(a, b))
print(obj.mul(a, b))
print(obj.div(a, b))