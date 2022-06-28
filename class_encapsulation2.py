class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def setAge(self, age):
        self.__age = age

    def tampilin(self):
        print(self.name)
        print(self.__age)
        print("----------")

orang_obj = Orang("budi", 30)

#akses melalui method
orang_obj.tampilin()

#akses melalui variabel langsung

#print(orang_obj.name)
#print(orang_obj.__age)

#engubah data tanpa setter tidak akan bisa
orang_obj.__age = 50
orang_obj.tampilin()

#merubah data harus dari setter

orang_obj.setAge(27)
orang_obj.tampilin()