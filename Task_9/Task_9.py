# Дана строка, в которой буква h встречается как минимум два раза. 
# Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке.

a = input()
a1 = a[:a.find('h')]
a2 = a[a.find('h'):a.rfind('h') + 1]
a3 = a[a.rfind('h')+ 1:]
print(a1 + a2[::-1] + a3)