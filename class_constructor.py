# dalam oop ada class constructor yang digunakan umumnya untuk membuat instance object
# tugas constructor adalah menetapkan nilai ke anggota data dari class ketika object dibuat
# dalam python kita bisa menggunakan __init__ method

class Car:
    def __init__(self, name, do):
        self.name = name
        self.do = do


avanza = Car('avanza', 'run to race')
brio = Car('Brio', 'run to pride')

print(avanza.name, avanza.do)
print(brio.name, brio.do)
