import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
    'Department' : ['HR','IT','FINANCE','IT','FINANCE','HR','HR','FINANCE','IT','FINANCE'],
    'salary' : [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000]
}
df=pd.DataFrame(data)
sns.set(style='whitegrid')

#create a box and whisker plot
plt.figure(figsize=(8,6))
sns.boxplot(data=df,x='Department',y='salary',palette='Set2')

#set title and label
plt.title("Box and whisker plot of a salary by Department")
plt.xlabel("Department")
plt.ylabel("salary")
plt.show()