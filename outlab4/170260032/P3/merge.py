import csv
import numpy as np

datad = np.genfromtxt('info_day.csv',dtype=None,delimiter=',').astype(str)
datan = np.genfromtxt('info_night.csv',dtype=None,delimiter=',').astype(str)
with open('info_combine.csv','w') as wfile:
    writer = csv.writer(wfile, delimiter=',', quotechar="'")
    writer.writerow(['Day', 'Temperature(Day)', 'Temperature(Night)', 'Humidity(Day)','Humidity(Night)','Light(Day)','Light(Night)','CO2(Day)','CO2(Night)'])
    datad1 = datad[1:]
    datan1 = datan[1:]
    for i in range(len(datad1)):
        writer.writerow([datad1[i][0][1:-1], datad1[i][1], datan1[i][1], datad1[i][2], datan1[i][2], datad1[i][3], datan1[i][3], datad1[i][4], datan1[i][4]])
