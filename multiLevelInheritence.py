#--- Multi Level Inheritene ---
class base1:
    def base1_fun(self):
        print("This is base1")

class base2(base1):
    def base2_fun(self):
        print("This is base2")

class base3(base2):
    def base3_fun(self):
        print("This is base3")


obj = base3()
obj.base1_fun()
obj.base2_fun()
obj.base3_fun()

