n = int(input("Ваше целое положительное число:"))
a = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > a:
        a = n % 10
    if n > 9:
        continue
    else:
        print(f"Максимальное число {a}")
        break
