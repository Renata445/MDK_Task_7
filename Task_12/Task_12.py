# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

a = input()
a1 = a[:a.find('h') + 1]
a2 = a[a.find('h') + 1:a.rfind('h')]
a3 = a[a.rfind('h'):]
print(a1 + a2.replace('h', 'H') + a3)