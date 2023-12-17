def main():
    A = [5, 3, 6, -2, 9, 12, -7, 15, 6, 8]  # Пример списка A из 10 элементов
    positive_multiples_of_3 = [num for num in A if num > 0 and num % 3 == 0]  # Выбираем положительные элементы, кратные 3
    product = 1
    count = 0

    for num in positive_multiples_of_3:
        product *= num  # Находим произведение положительных элементов, кратных 3
        count += 1  # Считаем количество найденных элементов

    print("Произведение положительных элементов, кратных 3:", product)
    print("Количество положительных элементов, кратных 3:", count)


if __name__ == "__main__":
    main()