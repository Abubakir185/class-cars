class Car:
    def __init__(self, speed, brend, color, year, nomi):
        self.speed = speed
        self.brend = brend
        self.color = color
        self.year = year
        self.nomi = nomi


    def stop(self):
        self.speed = 0
    
    def start(self):
        self.speed = 30
        

    def inc_speed(self):
        self.speed *= 1.4
    
    def dec_speed(self):
        self.speed -= 5

    def get_info(self):
        return f"Tezligi: {self.speed}, Brendi: {self.brend}, Rangi: {self.color}, yili: {self.year}, nomi: {self.nomi}"




    
class Matiz(Car):
    def __init__(self):
        super().__init__(50, "Chevrolet", "Yashil", 2020, "Matiz")   


matiz = Matiz()

print(matiz.speed)
matiz.inc_speed()
print(matiz.speed)
matiz.dec_speed()
print(matiz.speed)
matiz.stop()
print(matiz.speed)
print(matiz.get_info())


