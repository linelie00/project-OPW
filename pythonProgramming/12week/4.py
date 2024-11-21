class Car:
    wheels = 4
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def drive(self, km):
        self.mileage += km
        print(f'차량 색상 : {self.color}, 주행거리 : {self.mileage}km, 바퀴수 : {self.wheels}')

car1 = Car('Grey', 0)
car1.drive(10)
car2 = Car('Red', 15)
car2.drive(5)