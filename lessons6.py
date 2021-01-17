a = float(input('Сколько км в первый день: '))
b = float(input('Сколько км хотите достичь: '))
dist = a
day = 1
while dist < b:
    day += 1
    dist *= 1.1
print(f'Ваше достижение будет на : {day} день ({dist}км)')
