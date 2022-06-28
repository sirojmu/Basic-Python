print("=====Konversi Celcius=====")

celcius = float(input("Masukkan suhu dalam celcius: "))
fahrenheit = (9 / 5) * celcius + 32
reamur = (4 / 5) * celcius
kelvin = celcius + 273

print(celcius, "C adalah", fahrenheit, "F")
print(celcius, "C adalah", reamur, "R")
print(celcius, "C adalah", kelvin, "K")