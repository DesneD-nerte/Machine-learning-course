import numpy as np

N: int = int(input("Введите свой вариант: "))

initial_array = np.random.uniform(15, 37, (2,3,4))
print(initial_array)

string_array = np.array(initial_array, dtype=str)

string_array[initial_array < 20 * N] = "small"
string_array[initial_array > 30 * N] = "large"
string_array[(initial_array > 20 * N) & (initial_array < 30 * N)] = "medium"

print(string_array)
