# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу target_number.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число target_number


numb_of_elements = int(input('Введите количество элементов: '))
data = [int(i) for i in input("Введите числа: ").split()]
target_number = int(input("Введите искомое число:"))
nearest_neighbor = data[0]

for i in data:
    if abs(nearest_neighbor - target_number) > abs(i - target_number):
        nearest_neighbor = i
print("Ближайший сосед числа", target_number, ":", nearest_neighbor)










