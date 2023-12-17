def main():
    elements = [-5, 2, -3, 4, 5, 6, -7, 8, 9]  # Пример списка из вещественных элементов

    # 1. Номер минимального по модулю элемента списка
    min_abs_idx = min(range(len(elements)), key=lambda i: abs(elements[i]))
    print("Номер минимального по модулю элемента списка:", min_abs_idx)

    # 2. Сумма модулей элементов списка, расположенных после первого отрицательного элемента
    first_negative_idx = next((i for i, x in enumerate(elements) if x < 0), None)
    sum_abs_after_negative = sum(abs(x) for x in elements[first_negative_idx + 1 :] if x < 0)
    print("Сумма модулей элементов списка после первого отрицательного элемента:", sum_abs_after_negative)

    # Cжатие списка, удаление элементов в интервале [а, b] и заполнение оставшихся нулями
    a, b = -4, 4  # пример значений интервала [a, b]
    elements = [x if not (a <= x <= b) else 0 for x in elements]
    print("Сжатый список:", elements)


if __name__ == "__main__":
    main()