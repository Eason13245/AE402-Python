class Human():
    def __init__ (self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height

    def bmi(self):
        return self.weight//((self.height/100)**2)

    def perfectbody(self):
        bmi = self.weight//((self.height/100)**2)
        if 18 >= bmi <= 24:
            Reply = "You got the perfect body!!"
        elif bmi < 18:
            Reply = "You are unhealthy!!"
        elif bmi > 24:
            Reply = "You are so fat!!"
        else:
            Reply = "Please type the information properly!!"
            
        return Reply


a = Human("Ken", 63, 177)
print("name", a.name)
print("name", a.weight)
print("name", a.height)
print("BMI", a.bmi())
print(a.perfectbody())
