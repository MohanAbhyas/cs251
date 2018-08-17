import csv
import numpy as np

a = np.array
with open("info_day.csv",'r') as rfile:
    reader = csv.reader(rfile, delimiter=',')
  
    i = -1
    n=len(list(reader))
    a = np.zeros((n-1, 4))
   
with open("info_day.csv",'r') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    for row in reader:
        if i != -1:
            a[i][0] = row[1]
            a[i][1] = row[2]
            a[i][2] = row[3]
            a[i][3] = row[4]
        else:
            fields=row
            
        i = i+1
    mean = np.mean(a, axis = 0)
    stdd = np.std(a, axis = 0)
    
    print('{:<12s}{:>4s}{:>15s}'.format("Field","Mean","Std.Dev."))
    k=0
    while k<4:
        print('{:<12s}{:>4.3f}{:>10.3f}'.format(fields[k+1],round(mean[k],2),stdd[k]))
        k = k+1

    
