#Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения. 
# Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

a = input()
if a.count('f') >= 2:
    print(a.find('f', a.find('f') + 1))
elif a.count('f') == 1:
    print(-1)
else:
    print(-2)