class dog1:
    def sound(self):
        print("dog 1 barks low")

class dog2(dog1):
    def sound(self):
        print("dog 2 barks medium")

class dog3(dog1):
    def sound(self):
        print("dog 3 barks high")

dog = [dog1(), dog2(), dog3()]

for i in dog:
    i.sound()



