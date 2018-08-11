import csv
import numpy

data = numpy.genfromtxt('info_day.csv', dtype=None, delimiter=',').astype(str)
for i in data[1:]:
        i[1] = 32 + (9*float(i[1])/5)
with open('transformed.csv', 'w') as wfile:
    writer = csv.writer(wfile,delimiter=',',quotechar="'")
    for i in data:
        writer.writerow(i)

