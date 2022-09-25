# Дана строка X, возвращайте True, если X является палиндромом.
# Строка является палиндромом тогда, когда она читается одинаково как в обратном,
# так и в прямом направлении.
# Например, является “taco cat” является палиндромом,
# в то время как “black cat” не является.
# В данной задаче пробелы не учитываются.
# Гарантируется, что исходная строка может содержать символы только нижнего регистра.
# Пример 1:
# Ввод: x = “taco cat”
# Вывод: true
# Пояснение: “taco cat” читается, как “taco cat” слева направо так и справа налево.
# Пример 2:
# Ввод: x = “rotator”
# Вывод: true
# Пояснение: “rotator” читается, как “rotator” слева направо так и справа налево.
# Пример 3:
# Ввод: x = “black cat”
# Вывод: false
# Пояснение: слева направо она читается как “black cat” . Справа налево оно становится “tac kcalb”.
# Следовательно, это не палиндром.
# Для решения задачи рекомендуем познакомиться с функцией str.replace()

x = input("Введите строку\n")
x = x.replace(" ", '').casefold()
palindrom = True

for i in range(0, len(x)):
    if x[i] == x[len(x) - i - 1]:
        continue
    else:
        palindrom = False

print(palindrom)

