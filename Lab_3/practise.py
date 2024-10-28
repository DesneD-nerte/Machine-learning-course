import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

data = pd.read_csv("data/math_students.csv", delimiter=",")

# print(data[data.columns[:-1]].head())
data_without_result_column = data.drop(['G3'], axis=1).head()

plt.figure(figsize=(10,7))
plt.title("Absences distribution")
data["absences"].hist()
plt.xlabel('absences')
plt.ylabel('number of students')
plt.show()

print(data["absences"])

mean_absences = data['absences'].mean()
print('mean_absences:', mean_absences)

stud_few_absences = data[data['absences'] < mean_absences]
stud_many_absences = data[data['absences'] >= mean_absences]

print('Students with few absences:', stud_few_absences.shape[0])
print('Students with many absences:', stud_many_absences.shape[0])

stud_few_absences_g3 = stud_few_absences['G3'].mean()
stud_many_absences_g3 = stud_many_absences["G3"].mean()
print('Students with few absences, mean G3:', stud_few_absences_g3)
print('Students with many absences, mean G3:', stud_many_absences_g3)

data_by_school = data.groupby("school")
print(data_by_school.describe())

