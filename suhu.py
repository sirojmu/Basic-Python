def convert(celcius):
    fahrenheit = (9 / 5) * celcius + 32
    reamur = (4 / 5) * celcius
    kelvin = celcius + 273
    print(celcius, "C dalam reamur adalah", reamur, "R")
    print(celcius, "C dalam fahrenheit adalah", fahrenheit, "F")
    print(celcius, "C dalam kelvin adalah", kelvin, "K")
print(convert(float(input("Masukkan suhu dalam celcius:"))))