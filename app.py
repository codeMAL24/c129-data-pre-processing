import csv

data = []
with open("dataset_2.csv", "r")as f:
    c = csv.reader(f)
    for i in c:
        data.append(i)
headers = data[0]
planet_data = data[1:]

#Converting all planet names to lower case
for i in planet_data:
    i[2] = i[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2]) 
with open("data_sorted2.csv","a+")as f:
    cv = csv.writer(f)
    cv.writerow(headers)
    cv.writerows(planet_data)
    