import pandas as pd
import random
import numpy as np

def open_file(data):
    df = pd.read_csv(data, sep=" ", header=None)
    return df


def removeDuplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    return uniqueList

data = open_file('data.txt')


#odfiltrovanie uzlov

cities = []
cities = data[0].tolist() + data[1].tolist()
cities = removeDuplicates(cities)
r_city = random.sample(cities, 1)
print(r_city)

# vyber j uzlov

l = []
for index,row in data.iterrows():
    if row[0] == r_city or row[1] == r_city:
       l.append(row)

selected_data = pd.DataFrame(l)


tour = []
tour = selected_data.where(selected_data[2] == min(selected_data[2])).dropna()
tour = tour.values[0, :2].tolist()
tour = [int(i) for i in tour]
print(tour)


others = [x for x in cities if x not in tour]
print(others)










