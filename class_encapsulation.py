class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
    def tampilkan(self):
        print(self.name)
        print(self._age)

orang_obj = Orang("Budi", 30)

#akses melalui method
orang_obj.tampilkan()

#akses melalui variabel langsung
print(orang_obj.name)
print(orang_obj._age)

