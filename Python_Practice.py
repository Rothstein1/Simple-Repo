# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
Fifa19 = pd.read_csv("C:/Users/jacob/Fifa19.csv")
Fifa19 = Fifa19.set_index("Name")
Fifa19["Age"]= Fifa19["Age"] * -10 
Fifa19["Ag"]= 2 
 
StarFifa19WeakFoots = Fifa19.loc[(Fifa19.Composure >90) & (Fifa19.Marking >70) ]
Fifa19["Jewish?"]= "Yes"

StarFifa19WeakFoots= StarFifa19WeakFoots.rename(columns = {"Skill Moves": "SMoves" })

Fifa19.iloc[2,2]

reviews.country == 'Italy'
reviews.loc[reviews.country == 'Italy']

Fifa19.loc["L. Messi", "Potential"]

Fifa19.Age >20
yrs = Fifa19.loc[(Fifa19.Age ==30) & (Fifa19.Nationality == "Argentina")]
Fifa19.Nationality.describe()
help(Fifa19)
dir(Fifa19)

AGes =Fifa19.Age.unique()

AGes.sort()

AGes.type(List)

list = AGes.tolist()

list.sort(reverse=True)

Fifa19.Age.value_counts()
Fifa19_age_mean = Fifa19.Age.mean()

Years_above_avg= Fifa19.Age.map( lambda x : x- Fifa19_age_mean)
Years_above_avg_list = Years_above_avg.tolist()

Years_above_avg= Years_above_avg.sort_values()
yrs.Overall.describe()

Fifa19.Age- Fifa19_age_mean
Fifa19.Age.unique()

def remean_age(row):
    row.Age = row.Age - Fifa19_age_mean
    return row


x = Fifa19.apply(remean_age, axis ="columns")


def Overall_above20(row):
    row.Overall = row.Overall - 20
    return row


x = Fifa19.apply(Overall_above20, axis ="columns")

Overall_above20(1)



Fifa19.Nationality +"-" + Fifa19.Club
Fifa19_MeanAge = Fifa19.Age.mean()

x = Fifa19.Age.map(lambda q : q -Fifa19_MeanAge )

def remeanAge(row):
    row.Age = row.Age - Fifa19_MeanAge
    return row

y = Fifa19.apply(remeanAge, axis = "columns")

f= (Fifa19.Potential/Fifa19.Age).idxmax()
f.max()

f= (Fifa19.Potential/Fifa19.Age)

Bargain_idx = (Fifa19.Potential/Fifa19.Age).idxmax()



A = Fifa19.Nationality.map(lambda x: "a" in x).sum()

Not_A = Fifa19.Nationality.map(lambda x: "a" not in x).sum()

Total = A + Not_A
##Check
len(Fifa19) == Total


x = Fifa19.loc[(Fifa19.Potential >50)]












def Age(row):
    if row.Age >32:
        return "Old"
    elif row.Age >27:
        return "Mid age"
    elif row.Age >21:
        return "Young Man"
    else:
        return "Kid"
    
    
Fifa19["Age_Ratings"] = Fifa19.apply(Age, axis ="columns")

X = Fifa19.apply(Age, axis ="columns")

OverallByAge= Fifa19.groupby("Age").Overall.mean()




Fifa19.groupby("Age")

Fifa19.Nationality.iloc[1]

NationClub= Fifa19.groupby(["Nationality","Club" ]).apply(lambda x: x.loc[x.Overall.idxmax(), "ID" : "Overall"])

NationClub= Fifa19.groupby(["Nationality","Club" ]).apply(lambda x: x.loc[x.Overall.idxmin(), "ID": "Overall"])

NationClub_MaxPotential= Fifa19.groupby(["Nationality","Club" ]).apply(lambda y : y.loc[y.Potential.idxmax(), "ID": "Overall"])

Fifa19.Overall.idxmax()



PlayersNationality = Fifa19.groupby("Nationality").Overall.agg([len,min,max])


PlayersNationality= PlayersNationality.rename(columns = {"min": "Min Overall", "max":"Max Overall"})
Club_Nations = Fifa19.groupby(["Nationality", "Club"]).Overall.agg([len])
m = Club_Nations.index
type(m)

Club_Nations= Club_Nations.reset_index()
Club_Nations=Club_Nations.rename(columns = {"len": "# of players"})
x = Club_Nations.sort_values(by = "# of players", ascending = False)
x = Club_Nations.sort_index()
x= Club_Nations.sort_values(by = ["Nationality", "# of players"], ascending = False)

x= Fifa19.groupby(["Age", "Nationality"]).Overall.count().sort_values(ascending=False)



y= Fifa19.groupby(["Age", "Nationality"]).Potential.count()





