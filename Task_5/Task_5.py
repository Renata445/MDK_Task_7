#Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. 
# Если она встречается два и более раз, выведите индекс её первого и последнего появления. 
# Если буква f в данной строке не встречается, ничего не выводите.

a = input()
if a.count('f') == 1:
    print(a.find('f'))
elif a.count('f') >= 2:
    print(a.find('f'), a.rfind('f'))