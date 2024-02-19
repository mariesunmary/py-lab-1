def draw_pattern(N):
    for i in range(1, N+1):
        for j in range(i, N+1):
            print(j, end=" ")
        print()

# Перевірка введеного числа N
while True:
    try:
        N = int(input("Введіть ціле число N (1<N<9): "))
        if 1 < N < 9:
            break
        else:
            print("Число має бути в межах від 1 до 8.")
    except ValueError:
        print("Введено неправильне значення. Введіть ціле число.")

# Виведення рисунка
draw_pattern(N)
