from bs4 import BeautifulSoup
import requests
import csv
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page= requests.get(START_URL)
print(page)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all("table")
temp_list = []
table_rows = star_table[7].find_all("tr")
for tr in table_rows:
    td= tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

name_list = []
distance_list = []
mass_list = []
radius_list = []

for i in range(1,len(temp_list)):
    name_list.append(temp_list[i][0])
    distance_list.append(temp_list[i][5])
    mass_list.append(temp_list[i][8])
    radius_list.append(temp_list[i][9])

df2=pd.DataFrame(list(zip(name_list,distance_list, mass_list, radius_list)),columns=["star_name","distance","mass","radius"])

print(df2)
df2.to_csv("dwarf_stars.csv")
    
