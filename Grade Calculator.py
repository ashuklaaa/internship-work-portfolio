import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("StudentsPerformance.csv")
print(df.head())
print("Average math score:",df["math score"].mean())
print("Average reading score:",df["reading score"].mean())
print("Average writing score:",df["writing score"].mean())      
print("Average total score:",df[["math score","reading score","writing score"]].mean())

df["average score"] = df[["math score","reading score","writing score"]].mean(axis=1)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "E"
    else:
        return "F"

df["grade"] = df["average score"].apply(grade)

print(df.head())