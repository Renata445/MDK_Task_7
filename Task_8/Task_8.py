#Дана строка, в которой буква h встречается минимум два раза. 
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

a = input()
print(a[:a.find('h')] + a[a.rfind('h') + 1:])