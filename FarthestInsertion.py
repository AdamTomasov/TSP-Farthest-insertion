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

def remove_fromList(list):
    for x in list:
        if x == tour:
            list.remove(x)
    return (list)


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
tour = tour.values[0, :3].tolist()
tour = [int(i) for i in tour]
print(tour)


list_data = data.values.tolist()

df_u = pd.DataFrame(remove_fromList(list_data))
tour = pd.DataFrame(tour)


l = []
for idx, row in df_u.iterrows():
    if row[0] == tour[0][0] or row[0] == tour[0][1]:
        l.append(row.tolist())
    elif row[1] == tour[0][0] or row[1] == tour[0][1]:
        l.append(row.tolist())

df_c = pd.DataFrame(l)

select_maxTour = df_c.where(df_c[2] == max(df_c[2])).dropna()















