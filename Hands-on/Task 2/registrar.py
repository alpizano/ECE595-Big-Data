import pandas as pd

#f = open("students.txt", "r")

#for line in f:
    #print(line.strip())

#f.close()

df = pd.read_csv('students.txt', names=["STUDENT","COURSE","PERCENT","GRADE","CREDIT_HRS","GRADE_PTS","GPA"])
#df['GRADE'] = df['GRADE'].astype(str)

df['GPA'] = df['GPA'].astype(float)
df['CREDIT_HRS'] = df['CREDIT_HRS'].astype(float)
df['GRADE_PTS'] = df['GRADE_PTS'].astype(float)


# Display the grades for different subjects for each student
for i, row in df.iterrows():
    df.loc[i,'CREDIT_HRS'] = 3
    if row['PERCENT'] >= 90:
        df.loc[i,'GRADE'] = 'A'
        df.loc[i,'GRADE_PTS'] = 4
    elif 89 >= row['PERCENT'] >= 80:
        df.loc[i,'GRADE'] = 'B'
        df.loc[i,'GRADE_PTS'] = 3
    elif 79 >= row['PERCENT'] >= 70:
        df.loc[i,'GRADE'] = 'C'
        df.loc[i,'GRADE_PTS'] = 2
    elif 69 >= row['PERCENT'] >= 60:
        df.loc[i,'GRADE'] = 'D'
        df.loc[i,'GRADE_PTS'] = 1
    else:
        df.loc[i,'GRADE'] = 'F'
        df.loc[i,'GRADE_PTS'] = 0


#df['STUDENT'] = df['STUDENT'].astype('str')

print(df.dtypes)
print(len(df.index))

credits_sum =0

for i, row in df.iterrows():
    #df = df.groupby(['STUDENT']).sum().reset_index()
    #df.loc[i,'GPA'] = df.loc(df.groupby(['STUDENT'])['CREDIT_HRS'].agg('sum'))
    if i > 0:
        if df.loc[i,'STUDENT'] == df.loc[i-1,'STUDENT']:
            credits_sum = credits_sum + df.loc[i-1,'CREDIT_HRS']
            df.loc[i-1,'GPA'] = (credits_sum * df.loc[i-1, "GRADE_PTS"])/credits_sum
            print(sum)
        else:
            df.loc[i-1,'GPA'] = (credits_sum * df.loc[i-1, "GRADE_PTS"])/credits_sum
            credit_sum = 0
    if i == len(df.index)-1:
        df.loc[i,'GPA'] = (credits_sum * df.loc[i, "GRADE_PTS"])/credits_sum


#for i,row in enumerate(df.itertuples(),0):
#    df.at[i,'CREDIT_HRS'] = 3
#    if row.PERCENT >= 90:
 #       df.at[i,'GRADE'] = 'A'
 #       df.at[i,'GRADE_PTS'] = 4
#    elif 89 >= row.PERCENT >= 80:
#       df.at[i,'GRADE'] = 'B'
#    elif 79 >= row.PERCENT >= 70:
#        df.at[i,'GRADE'] = 'C'
#    elif 69 >= row.PERCENT >= 60:
#        df.at[i,'GRADE'] = 'D'
#    else:
#        df.at[i,'GRADE'] = 'F'
#    df.at[i,'GPA'] = row.CREDIT_HRS * row.GRADE_PTS


print(df)
print("\nThe highest scores and scorers in each subject:")

# Display the highest score and scorer in each subject

#print(df.loc[df.groupby('COURSE')['PERCENT'].idxmax()])
top_scorers = df.loc[df.groupby('COURSE')['PERCENT'].idxmax()]
print(top_scorers.iloc[0:3, 0:3])

print("\nThe GPA of each student")
#print((df.groupby(['STUDENT'])['CREDIT_HRS'].agg('sum')*df.groupby(['STUDENT'])['GRADE_PTS'].agg('sum'))/df.groupby(['STUDENT'])['CREDIT_HRS'].agg('sum'))
#print(df.groupby(['STUDENT'])['CREDIT_HRS'].agg('sum').reset_index(name='GPA'))
