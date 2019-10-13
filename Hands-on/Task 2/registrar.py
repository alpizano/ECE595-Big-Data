import pandas as pd

f = open("students.txt", "r")

for line in f:
    print(line.strip())

f.close()

df = pd.read_csv('students.txt', names=["name","class","percent","grade"])



for i, row in df.iterrows():
    if row['percent'] >= 90:
        df.loc[i,'grade'] = 'A'
    elif 89 >= row['percent'] >= 80:
        df.loc[i,'grade'] = 'B'
    elif 79 >= row['percent'] >= 70:
        df.loc[i,'grade'] = 'C'
    elif 69 >= row['percent'] >= 60:
        df.loc[i,'grade'] = 'D'
    else:
        df.loc[i,'grade'] = 'F'



print(df)
