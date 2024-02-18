
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_product_and_count(arr):
    product = 1
    count = 0

    for num in arr:
        if num > 8 and num < 18 and num % 10 == 0:
            product *= num
            count += 1

    return product, count

# Ввод списка А из 10 элементов
A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

# Нахождение произведения элементов, удовлетворяющих условиям, и их количества
result_product, result_count = calculate_product_and_count(A)

print(f"Произведение элементов, больших 8, меньших 18 и кратных 10: {result_product}")
print(f"Количество таких элементов: {result_count}")
