# На вход подаются две строки X1 и X2, содержащие бинарные числа.
# Необходимо вывести их бинарное произведение в формате строки.
#
# Пример 1:
# Ввод: x1 = ‘’111” и x2= “101”
# Вывод: “100011”
# Пояснение: “111” - это 7; “101” - это 5; 7*5 = 35; 35 в двоичной системе 100011
#
# Гарантируется, что введенная строка X будет содержать только числа 1 и 0.

firstnumber = input()
secondnumber = input()

firstnumber = str(firstnumber)
secondnumber = str(secondnumber)

Multiplication = int(firstnumber, 2) * int(secondnumber, 2)
binaryMul = bin(Multiplication)

print(binaryMul.replace("0b",''))