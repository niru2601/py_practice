import pandas as pd

data = {'names':['Boston Celtics', 'Amir Johnson', 'R.J. Hunter','ketan','niranjan'],
        'age':[10,20,10,20,10]}
# Making data frame from the csv file
df = pd.DataFrame(data)

df1 = df['names'].replace(['Boston Celtics', 'Amir Johnson', 'R.J. Hunter'],
                 ['Omega Warriors', 'Mitcell Johnson', 'Shivang Thomas'])
print(df)
print(df1)