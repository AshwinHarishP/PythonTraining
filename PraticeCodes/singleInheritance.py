#----Single Inheritance -> One Base Class and One Derived Class ----

class base:   

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("Base Class of display")
        print("Name: ", self.fname + " " +self.lname)

class derived(base):

    def display2(self):
        print("Derived Class of display")

    def display1(self):
        print("Derived Class of display1")


obj1 = derived("Ashwin", "Harish")
obj1.display()

