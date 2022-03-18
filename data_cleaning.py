import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\ericlaub\OneDrive - The Meyocks Group, Inc\Documents\Python Scripts\yg821jf8611_fl_statewide_2020_04_01.csv\data.csv",low_memory=False)

print(df.columns.values)
for i in df.columns.values:
    print(i)

df = df[df['subject_race'].notna()]
df = df[df['officer_race'].notna()]
df = df[df['raw_EnforcementAction'].notna()]
df = df[df['subject_age'].notna()]
df = df[df['raw_EnforcementAction'].notna()]

df = df.drop(columns=['raw_row_number_old', 'raw_Race','raw_row_number_new'])

df1 = df[['officer_race','subject_race','officer_age', 'subject_age', 'subject_sex','officer_sex','officer_years_of_service','outcome']]

df1= df1.dropna()
df1 = df1.sample(n=100000)
df1 = df1.reset_index(drop=True)
df1['severity'] = 0
for i in range(len(df1['severity'])):
    if df1['outcome'][i] == 'arrest':
        df1['severity'][i] = 3
    elif df1['outcome'][i] == 'citation':
        df1['severity'][i] = 2
    elif df1['outcome'][i] == 'warning':
        df1['severity'][i] = 1


df1 = pd.get_dummies(df1)