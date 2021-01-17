numb_1 = int(input("Выручка вашей фирмы: "))
numb_2 = int(input("Издержки фирмы: "))

if numb_1 > numb_2:
    pribl = numb_1 - numb_2
    print(f"Чистый прибль: {pribl}")
    numb_3 = int(input("Сколько работающего персонала: "))
    sotrud = pribl // numb_3
    print(f"Прибыль на каждого сотрудника: {sotrud}")
elif numb_1 < numb_2:
    pribl1 = numb_1 - numb_2
    print(f"Вашей фирме издержки больше выручки: {pribl1}")
