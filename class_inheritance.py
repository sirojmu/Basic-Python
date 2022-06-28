class Person:
    nama = 'Test'

class Employee(Person):
    gaji = 100000000000

person1 = Person()
employee1 = Employee()

print('Nama dari person', person1.nama)
print('nama dari employee', employee1.nama)
print('gaji employee', employee1.gaji)
print('gaji person', person1.gaji)
