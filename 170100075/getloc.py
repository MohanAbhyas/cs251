#! /usr/local/bin/python
import json
import requests
import datetime
def iss_location():
	url="http://api.open-notify.org/iss-now.json"
	wbpage=requests.get(url)
	obj=json.loads(wbpage.content) 
	print("Current Location of ISS:")
	print("Latitude :",obj["iss_position"]["latitude"])
	print("Longitude :",obj["iss_position"]["longitude"])
def pass_time():
	url2="http://api.open-notify.org/iss-pass.json"
	param={}
	request={}
	print("Enter Details to know when ISS will pass over a location:")
	request["latitude"]=float(input("Latitude :"))
	request["longitude"]=float(input("Longitude :"))
	param["request"]=request

	#wbpage1=requests.post(url,request)
	print(request)
	wbpage=requests.get(url2,params=request)
	print(wbpage.text)
def people_info():
	url3="http://api.open-notify.org/astros.json"
	wbpage3=requests.get(url3)
	obj3=json.loads(wbpage3.content)
	print("People currently in space:",obj3["number"])
	for people in obj3["people"]:
		print(people["name"])
iss_location()
pass_time()
people_info()

