import pandas as pd
import re

pd.set_option("display.max_columns", None)

data = pd.read_csv('data/titanic.csv')

# 1
women_count = data[data["Sex"] == "female"].shape[0]
men_count = data[data["Sex"] == "male"].shape[0]
print("Количество женщин:", women_count)
print("Количество мужчин:", men_count)

# 2
survived_count = data[data["Survived"] == 1]["Survived"].value_counts()
percent_survived_count = survived_count / len(data)
print("Количество всех пассажиров:", len(data))
print("Количество выживших пассажиров:", survived_count.sum())
print("Доля выживших пассажиров:", round(percent_survived_count.sum(), 2))

# 3
first_class_count = data[data["Pclass"] == 1]["Pclass"].value_counts()
percent_first_class = first_class_count / len(data)

print("Количество всех пассажиров:", len(data))
print("Количество пассажиров: первого класса", first_class_count.sum())
print("Доля пассажиров первого класса среди всех пассажиров:", round(percent_first_class.sum(), 2))


# 4
average_age = data['Age'].mean()
median_age = data['Age'].median()

print("Средний возраст пассажиров:", average_age)
print("Медианный возраст пассажиров:", median_age)

# 5
correlation_sibsp_parch = data['SibSp'].corr(data['Parch'], method='pearson')

print("Корреляция Пирсона между SibSp и Parch:", correlation_sibsp_parch)


# 6

# В случае Mrs. пытаемся вытащить первое слово из скобок, иначе последующее слово
# В случае Miss. ытаемся вытащить последующее слово
# Иначе возвращаем None
def extract_female_first_name(full_name: str):
    if("Mrs." in full_name):
        match = re.search(r'\(([^)]+)\)', full_name)
        if(match):
            return match.group(1).split()[0]
        else:
            return full_name.split("Mrs.")[1].strip().split()[0]
    if("Miss." in full_name):
        return full_name.split("Miss.")[1].strip().split()[0]

    return None

# print(extract_female_first_name("Cumings, Mrs. John Bradley (Florence Briggs Thayer) test (1231)"))
# print(extract_female_first_name("Heikkinen, Miss. Laina"))
# print(extract_female_first_name("Masselmani, Mrs. Fatima test"))

data["Firstname"] = data[data["Sex"] == "female"]["Name"].apply(extract_female_first_name)
most_common_women_name = data["Firstname"].value_counts().idxmax()
print("Самое популярное женское имя на корабле:", most_common_women_name)