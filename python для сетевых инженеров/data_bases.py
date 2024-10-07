import pandas as pd 
import numpy as np 

s = pd.Series(np.arange(5), index=["a",'b','c',"d","e"])
s = pd.Series(np.linspace(0,1,11))


d = {'a': 10, "b":20,'c':30,'d':40}
#print(pd.Series(d))

a = ['a','b','c']
#print(pd.Series(5,index=a))

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
#print("Выбор одного элемента")
#print(s["a"])
#print("Выбор нескольких элементов")
#print(s[["a", "d"]])
#print("Срез")
#print(s[3:])
#print("Поэлементное сложение")
#print(s + s)

#print('Фильтрация')
s.name = 'Имя'
s.index.name = 'Индекс'
#print(s[s>=2])


students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pd.DataFrame(students_marks_dict)
students.index = ['A',"B","C"]
#print(students)

#print(students.loc["B":])


student = pd.read_csv("StudentsPerformance.csv")
print(student)