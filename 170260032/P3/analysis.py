import csv
import numpy as np

a = np.array
with open("info_day.csv",'r') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    n = 0
    for row in reader:
        n = n+1
    a = np.zeros((n-1, 4))
    i = -1
with open("info_day.csv",'r') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    for row in reader:
        if i != -1:
            a[i][0] = row[1]
            a[i][1] = row[2]
            a[i][2] = row[3]
            a[i][3] = row[4]
        i = i+1
    mean = np.mean(a, axis = 0)
    stdd = np.std(a, axis = 0)
    print("Field      ","Mean  ","Std.Dev.")
    print("Temperature",round(mean[0],2),"",stdd[0])
    print("Humidity   ",round(mean[1],2),"",stdd[1])
    print("Light      ",round(mean[2],2),stdd[2])
    print("CO2        ",round(mean[3],2),stdd[3])
