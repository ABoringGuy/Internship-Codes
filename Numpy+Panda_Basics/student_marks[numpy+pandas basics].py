import numpy as np
import pandas as pd

number_of_students=int(input("Enter number of students:"))
subjects=["science","math","english"]
students=[]

for i in range(number_of_students):
    students.append(f"student {i}")
marks=np.empty((number_of_students, len(subjects)), dtype=np.int32)

def user_input():
    science_marks=int(input("Enter science marks:"))
    math_marks=int(input("Enter math marks:"))
    english_marks=int(input("Enter english marks:"))
    return science_marks,math_marks,english_marks

for student in range(number_of_students):
    print("Enter Marks for Student ",student)
    marks[student]=user_input()

data_frame=pd.DataFrame(marks, columns=subjects, index=students)
print(data_frame)

"""Axis 0 means go through Column, Axis 1 means go through Row"""
data_frame["Average"]= data_frame.mean(axis=1)
print(data_frame)

data_frame["Result"]= np.where((data_frame[subjects]>50).all(axis=1), "Pass", "Fail")
print(data_frame)

"""The code below works as such:
data_frame["Result"] == Pass, returns a boolean mask based on which student has Passed or Failed.
If 3 students [pass, fail, pass] then data_frame["Result"] == Pass returns [true, false, true].
Now, data_frame[data_frame["Result"] == "Pass"], here the outer data_frame give result based on mask.
Meaning it shows results for only 'true' value"""

passed_students = data_frame[data_frame["Result"] == "Pass"]
print(passed_students)