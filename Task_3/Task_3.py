#Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
# то длина первой части должна быть на один символ больше). Переставьте эти две части местами, 
# результат запишите в новую строку и выведите на экран.

#При решении этой задачи не стоит пользоваться инструкцией if.

a = input()
print(a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])