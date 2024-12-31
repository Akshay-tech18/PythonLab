import pandas as pd
data = {'Name':['Alia','Bob','Charli',None,'eve'],
        'Age' : [25,None,30,22,None],
        'City' : ['New york','Los angels',None,'Chicago','Miami']
        }

df=pd.DataFrame(data)

def analyze_missing_data(df):
    print("DataFrame:")
    print(df)
    print("\n missing data analysis : ")

    missing_data = df.isnull().sum()
    print("Missing values in each column: ")
    print(missing_data[missing_data>0])

    missing_percentage=(missing_data/len(df))*100
    print("\n Percentage of missing values in each column : ")
    print(missing_percentage[missing_percentage>0])
    return missing_data,missing_percentage

def handle_missing_data(df):
    print("\n Choose a method to handle missing data ")
    print("1. Fill missing values with specified value")
    print("2. Drop rows with missing values")
    print("3. Drop columns with missing data")
    choice = input("Enter your choice (1/2/3): ")
    if choice=='1':
        value=input("Enter the value to fill missing data : ")
        df_filled=df.fillna(value)
        print("Data after filling missing values.")
        print(df_filled)
    elif choice=='2':
        df_dropped_rows=df.dropna()
        print("\n Data after dropping row with missing values : ")
        print(df_dropped_rows)
    elif choice=='3':
        df_dropped_columns=df.dropna(axis=1)
        print("\n Data after dropping columns with missing values : ")
        print(df_dropped_columns)
    else:
        print("Invalid choice !!! please enter 1 or 2 or 3 ")

missing_data,missing_percentage = analyze_missing_data(df)
handle_missing_data(df)
