class Hewan():
    def suara(self):
        print("Suara hewan")


class Kucing():
    def suara(self):
        print("Meoooowww")

    def harapan_hidup(self):
        print("Harapan hidup kucing adalah 10 tahun")

    def warna_tubuh(self):
        print("umumnya kucing berwarna oren")


class Anjing():
    def suara(self):
        print("Gukgukguk")

    def harapan_hidup(self):
        print("Harapan hidup anjing adalah 15 tahun")

    def warna_tubuh(self):
        print("umumnya anjing berwarna hitam")


obj1 = Kucing()
obj2 = Anjing()
for type in (obj1, obj2):
    type.harapan_hidup()
    type.warna_tubuh()
    type.suara()
