import pandas as pd
import random

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

print(cities)

