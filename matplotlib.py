import pandas as pd
import matplotlib.pyplot as plt

data={
    'Age' : [25,30,35,40,45,50,55,60,65,70],
    'Salary' : [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000],
    'Department' : ['HR','IT','Finance','IT','Finance','HR','HR','Finance','IT','Finance']
}
df=pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.scatter(df['Age'],df['Salary'],color='blue',marker='o')
plt.title("Scatter plot of age vs salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['Age'],bins=5,color='green',edgecolor='black')
plt.title("Histogram of Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(8,5))
department_counts = df['Department'].value_counts()
plt.bar(department_counts.index,department_counts.values,color='orange',edgecolor='black')
plt.title("Bar plot pf department counts")
plt.xlabel("Department")
plt.ylabel("Number of employees")
plt.grid(axis='y')
plt.show()