#jika nilai variabel dari objek ke objek bervariasi maka variabel tersebut disebut dengan instance variabel
#instance variable tidak dibagikan oleh object. setiap object memiliki salinan sendiri dari instance atribut
#artinya untuk setiap instance dalam suatu kelas, memiliki nilai instance variabel yang berbeda
class Circle:
    def __init__(self, name, radius, Pi):
        self.__name = name #instance variable
        self.__radius = radius #instance variabel
        self.__pi = Pi

    #untuk menghitung luas lingkarang digunakan pi*r^2

    def area(self):
        return self.__pi*self.__radius**2

c1 = Circle("C1", 4, 3.14)
print("luas area C1 adalah", c1.area())
c2 = Circle("C2", 5, 3.141567890)
print("luas area C2 adalah", c2.area())
c3 = Circle("C3", 6, 22/7)
print("luas area C3 adalah", c3.area())