class dog:
    def __init__(self,name,color):
        self.name= name
        self.color = color

    def display_name(self):
        print(f"My dog name is {self.name}")

class dog1(dog):
    def reaction(self):
        print(f"{self.name} is barking")


class dog2:
    def clr(self):
        print(f"color is {self.color}")
    
class dog3(dog,dog2):
    def multiple_inherit(self):
        pass

# dg = dog1("buddy")
# dg.display_name()
# dg.reaction()

dg1= dog3("kevin","white")
dg1.display_name()
dg1.clr()
