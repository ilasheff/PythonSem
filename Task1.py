# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

from_user = int(input("Введите число от 1 до 7: "))

if from_user > 7:
    print("Вы ввели число больше 7")
else:
    print(f"{from_user} -> {from_user == 6 or from_user == 7}")