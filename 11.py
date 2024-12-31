import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
    'Age' : [25,30,35,40,45,50,55,60,65,70],
    'salary' : [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000],
    'Department' : ['HR','IT','FINANCE','IT','FINANCE','HR','HR','FINANCE','IT','FINANCE']
}

df=pd.DataFrame(data)
sns.set(style='whitegrid')

#scatter plot of age vs salary
plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x='Age',y='salary',hue='Department',palette='viridis',s=100)
plt.title("scatter plot of age vs salary")
plt.xlabel("Age")
plt.ylabel("salary")
plt.legend(title='Department')
plt.show()

#Histogram of age distribution
plt.figure(figsize=(8,5))
sns.histplot(data=df,x='Age',bins=5,kde=True,color='purple')
plt.title("Histogram of Age distribution ")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#Bar plot of department counts
plt.figure(figsize=(8,5))
sns.countplot(data=df,x='Department',palette='pastel')
plt.title("Bar plot of department counts")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()