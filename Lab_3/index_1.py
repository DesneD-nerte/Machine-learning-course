import matplotlib.pyplot as plt
import pandas as pd

pd.set_option("display.max_columns", None)

data = pd.read_csv('data/math_students.csv')

# 1
max_reason_value = data["reason"].value_counts().idxmax()
print("Самая частая причина выбора школы: ", max_reason_value)

# 2
no_education_count = data[(data['Medu'] == 0) & (data['Fedu'] == 0)].shape[0]
print("Количество студентов, с родителями без образования: ", no_education_count)

only_one_education_count = data[(data['Medu'] == 0) | (data['Fedu'] == 0)].shape[0]
print("Количество студентов, у которых хотябы один родитель не имеет образование: ", only_one_education_count)

# 3
lowest_age_from_Mousinho_school = data[data["school"] == "MS"]["age"].min()
print("Минимальный возраст учащегося школы Mousinho da Silveira: ", lowest_age_from_Mousinho_school)

# 4
odd_absence_student_counts = data[data["absences"] % 2 != 0].shape[0]
print("Количество студентов, имеющих нечетное число пропусков: ", odd_absence_student_counts)

# 5
romantic_mean = data[data["romantic"] == "yes"]["G3"].mean()
non_romantic_mean = data[data["romantic"] == "no"]["G3"].mean()
differences_between_romantic_and_g3 = abs(romantic_mean - non_romantic_mean)
print("Состоящие в отношениях:", romantic_mean)
print("Не состоящие в отношениях:", non_romantic_mean)
print("Разность между средними итоговыми оценками студентов, состоящих и не состоящих в романтических отношениях: ", round(differences_between_romantic_and_g3, 2))

# 6
max_activities_value = data["activities"].max()
all_students_with_max_activities_value = data[data["activities"] == max_activities_value]
max_absences_with_max_activities_value = all_students_with_max_activities_value["absences"].value_counts().idxmax()
print("Часто ли внекласнные активности :", max_activities_value)
print("Занятий пропустило большинство студентов с самым частым значением наличия внеклассных активностей :", max_absences_with_max_activities_value)
