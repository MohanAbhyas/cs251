#! /usr/local/bin/python
import csv
import sqlite3
def returnCount() :
	cat=input()
	conn = sqlite3.connect('cse_students.sqlite')
	c=conn.cursor()
	c.execute("SELECT [No. of students] FROM cse_students where [Category Name]=?",[cat])#no of students and category name should be replaced by header, but wasn't able to 
	i=c.fetchall()
	if len(i)==0:
		print("INVALID")
	else:
		for j in i:
			print(int(str(j).replace(',)','').replace('(','').replace('\'','')))
#can be improved, tried a lot but couldn't succeed

	conn.close()




with open('count.csv','r') as f:
	header=f.readline().replace('\n','').split(',')
	reader=csv.reader(f,delimiter=',')
	category=[]
	stud=[]
	for row in reader:
		category.append(row[0])
		stud.append(row[1])

conn = sqlite3.connect('cse_students.sqlite')
c=conn.cursor()
c.execute("create TABLE cse_students {}".format(tuple(header)))


i=0
while i < len(category):
	c.executemany('INSERT INTO cse_students VALUES (?,?)', [(category[i],stud[i])])
	i=i+1

conn.commit()
conn.close()
returnCount()
