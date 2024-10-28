def found_bmi_description_by_age(bmi: float, age: int):
    lowest_limit: float = 18.5 if (age < 45) else 22
    normal_limit: float = 25 if (age < 45) else 27
    biggest_limit: float = 30 if (age < 45) else 32

    if (bmi < lowest_limit):
        return "Недостаточная масса тела"
    if (bmi >= lowest_limit and bmi < normal_limit):
        return "Нормальная масса тела"
    if (bmi >= normal_limit and bmi < biggest_limit):
        return "Избыточная масса тела"
    if (bmi >= biggest_limit):
        return "Ожирение"

    return "Категория не определена"


age: int = int(input("Введите свой возраст: "))
weight: float = float(input("Введите свой вес: "))
height: float = float(input("Введите свой рост (в сантиметрах): ")) / 100

# Подсчет индекса и категории происходит без округления для точного подсчета. Округляем только при демонстрации пользователю
bmi: float = weight / height ** 2
category_description = found_bmi_description_by_age(bmi, age)

print(f'Возраст: {age}\n'
      f'Вес: {weight}\n'
      f'Рост: {height}\n'
      f'Индекс массы тела: {round(bmi, 2)}\n'
      f'Категория: {category_description}')
