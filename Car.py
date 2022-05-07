class Car :
    def __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def __str__(self):
        return print(self.brand +" "+ self.model + " "+ self.year + " "+self.color)
    
    def honk(self):
        print('honk honk !')

myCar01 = Car('ford','T','1920','black')
myCar01.honk()
print(myCar01.brand + " " + myCar01.model + " " + myCar01.year + " " + myCar01.color)