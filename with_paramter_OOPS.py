# --- class, Object -- 

# Class
class one:
    self.name = name
    self.marks = marks
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   

    def display(self):
        print(self.name)
        print(self.marks)


# Object

obj1 = one("Ashwin", 100)
obj1.display()

print(obj1.name) #Internally: self.name which is "Ashwin"

obj1.name = "Aravind" #Internally: self.name = "Aravind"
obj1.marks = 101      #Internally: self.marks = 101

print(obj1.name)    #Internally: self.name which is "Aravind"
print(obj1.marks)   #Internally: self.marks which is 101

