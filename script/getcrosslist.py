import pandas as pd
from uiuccourses import *

# load in csv from https://github.com/illinois/courses-dataset
courses = pd.read_csv("data/2019-fa.csv", header=0)

df = pd.DataFrame(columns=['Course', 'Equivalent'])

rows = len(courses.index)
for x in range(0, rows):
    descrip = courses.loc[x, 'Description']
    if type(descrip) is str: # do not parse empty / non-string rows
        crosslists = sameAsCode(descrip)

        for c in crosslists:
            df = df.append({'Course': (courses.loc[x, 'Subject'] + " " + str(courses.loc[x, 'Number'])), 'Equivalent': c}, ignore_index=True)

df.to_csv("crosslisted-courses.csv", index=False)
