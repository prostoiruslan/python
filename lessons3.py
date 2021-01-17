number = int(input('Введите целое число: '))
numb_1 = int("%s" % number)
numb_2 = int("%s%s" % (number,number))
numb_3 = int("%s%s%s" % (number,number,number))


print(numb_1 + numb_2 + numb_3)

