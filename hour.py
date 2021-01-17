numb_1 = int(input("Введите время в секундах: "))

hour = numb_1 // 3600
hour1 = numb_1 % 3600

minute = hour1 // 60
minute1 = hour1 % 60

print(f"{hour}:{minute}:{minute1}")