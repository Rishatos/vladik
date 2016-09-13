# -*- coding: utf-8 -*-
print u"Если число будет кратное 3. Пишем слово Fizz."
print u"Если число будет кратное 5. Пишем слово Buzz."
print u"В данном случае используются числа от 1 до 100.“
one = 1
zero = 0
a = 0
lol = 100
while a < lol:
    print a
    a = a + 1
    if a // 3:
        print "Fizz"
    elif a // 5:
        print "Buzz"
    else:
        print a

