while True:
    try:
        count = input("Введите количество чисел: ")
        choose = input("Введите действие( + | - | * | / ): ")

        for i in range(int(count)):
            number = int(input("Введите " + str(i + 1) + " число: "))

            if i == 0:
                result = number
                continue

            if choose == "+":
                result = result + number
            if choose == "-":
                result = result - number
            if choose == "*":
                result = result * number
            if choose == "/":
                result = result / number

        print(result)
    except:
        print("Ошибка!")

        continue