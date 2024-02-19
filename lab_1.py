def main():
    # Введення чисел a та b з клавіатури
    a = float(input("Введіть значення a (додатнє число): "))
    b = float(input("Введіть значення b (додатнє число): "))

    # Перевірка на додатність чисел a та b
    if a <= 0 or b <= 0:
        print("Числа повинні бути додатніми.")
        return

    # Обчислення значення X згідно з умовою
    if a > b:
        X = 5 * a + b
    elif a == b:
        X = -125
    else:
        X = (a - 5) / b

    # Виведення результату
    print("Значення X дорівнює", X)

if __name__ == "__main__":
    main()