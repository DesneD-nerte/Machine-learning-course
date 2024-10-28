import numpy as np

my_array = np.loadtxt('data/iris.csv', delimiter=',', skiprows=1)

array = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

N: int = int(input("Введите свой вариант: "))

# Умножение каждого элемента массива на число
multiplied_array = my_array * N
columns_sum = multiplied_array.sum(axis=0)
print(f"Умножение элементов массива на {N}: {columns_sum}")

# Элементы массива my_array, которые больше трех*N и меньше 5*N одновременно
# i = np.logical_and(my_array > 3 * N, my_array < 5 * N)
# print(my_array[i])
range_array = my_array[(my_array > 3 * N) & (my_array < 5 * N)]
print(f"Элементы массива в диапазоне {3*N} и {5*N}: {range_array}")

# Новый двумерный массив из случайных чисел той же размерности, что и my_array.
my_generated_array = np.random.randint(1, 500, my_array.shape)
print(my_generated_array)

# Поэлементное умножение элементов.
result_array = my_array * my_generated_array
