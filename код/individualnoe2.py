#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def process_list(input_list):
    # 1. Подсчет отрицательных элементов
    neg_count = sum(1 for num in input_list if num < 0)

    # Находим минимальный элемент по модулю и его индекс
    min_abs_value = min(map(abs, input_list))
    min_abs_index = input_list.index(min_abs_value) if min_abs_value in input_list else input_list.index(-min_abs_value)

    # 2. Вычисляем сумму модулей элементов после минимального по модулю элемента
    sum_after_min = sum(abs(num) for num in input_list[min_abs_index+1:])

    # Замена отрицательных элементов и сортировка списка по возрастанию
    modified_list = [num**2 if num < 0 else num for num in input_list]
    modified_list.sort()

    return neg_count, sum_after_min, modified_list

# Ввод списка вещественных элементов
input_list = [float(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

# Обработка списка
neg_count, sum_after_min, sorted_list = process_list(input_list)

print(f"Количество отрицательных элементов: {neg_count}")
print(f"Сумма модулей элементов после минимального по модулю элемента: {sum_after_min}")
print(f"Измененный и отсортированный список: {sorted_list}")

