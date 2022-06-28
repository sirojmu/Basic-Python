num1 = float(input("Masukkan angka: "))
num2 = float(input("Masukkan angka: "))
operator = input("Masukkan operator: ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1/num2)
elif operator == '*':
    print(num1 * num2)
else:
    print("Invalid operator!")

