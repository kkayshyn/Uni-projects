import pandas as pd
import numpy as np

data = {
    'animal': ['cat', 'dog', 'cat', 'snake', 'dog', 'dog', 'cat', 'cat', 'dog', 'dog'],
    'name': ['Daisy', 'Bella', 'Noodle', 'Milo', 'Charlie', 'Max', 'Cooper', 'Luna', 'Rocky', 'Buddy'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a','b','c','d','e','f','g','h','i','j']

animals = pd.DataFrame(data, index=labels)

#ZADANIE 1
#animals.info()
#print(animals.describe())
print(animals)

#ZADANIE 2
print(animals.head(3))
print(animals[['animal', 'age']])
print(animals.loc[['d', 'e', 'i'], ['visits', 'priority']])
print(animals[animals['visits'] > 2])
print(animals[(animals['animal'] == 'cat') & (animals['age'] < 4)])
print(animals[animals['age'].between(2, 4)])

#ZADANIE 3
animals.loc['k'] = ['dog', 'Buddy', 5.5, 2, 'no']
animals['price'] = animals['priority'].map({'no': 10, 'yes': 20})
animals['total'] = animals['visits'] * animals['price']
animals.drop(columns='priority', inplace=True)
animals.rename(columns={'animal': 'species'}, inplace=True)
print(animals)

#ZADANIE 4
animals.reset_index(drop=True, inplace=True)
print(animals)
animals.set_index('name', inplace=True)
print(animals)
animals.drop(index='Max', inplace=True)
print(animals)
animals.reset_index(inplace=True)
print(animals)

#ZADANIE 5
animals['species'] = animals['species'].str.upper()
print(animals)
animals.to_csv('animals.csv', index=False)
