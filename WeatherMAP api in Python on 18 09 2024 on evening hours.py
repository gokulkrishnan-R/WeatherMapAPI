#***************************** Making this in OOPS Concept *****************************
#***************************** Virtual Env name = "api_boi" *********************************
#***************************** WeatherMap API using RESTAPI's *********************************

import json
import requests as request
import csv

class WeatherMap():

	def __init__(self,city_name,API_KEY,BASE_URL,url,response,data,main,description,current_temperature,pressure,humidity,co_ordinates,sno):
		print("\n")
		self.city_name=str(input("Enter the city name:"))
		self.API_KEY=API_KEY
		self.BASE_URL=BASE_URL
		self.url=url
		self.response=response
		self.data=data
		self.main=main
		self.description=description
		self.current_temperature=current_temperature
		self.pressure=pressure
		self.humidity=humidity
		self.co_ordinates=co_ordinates
		self.sno=sno

	def get_city_name(self):
		#Creating urls from base urls
		self.url=f"{self.BASE_URL}?q={self.city_name}&appid={self.API_KEY}&units=metric"
		#Getting the request to the url
		self.response=request.get(self.url)
		# Check if the response is successfull
		if self.response.status_code!=404:
			#Instaziating variables in json format
			self.data=self.response.json()
			#Extracting useful data
			#Here we are assigingn data to main variaable and acessing all the datas through "main" key.
			self.main=self.data["main"]
			self.weather_description=self.data["weather"][0]["description"]
			self.current_temperature=self.main["temp"]
			self.pressure=self.main["pressure"]
			self.humidity=self.main["humidity"]
			self.co_ordinates=self.data["coord"]

			print("\n")
			print(f"City_name:{self.city_name}\n")
			print(f"Weather_Description:{self.weather_description}\n")
			print(f"Current_Temperature:{self.current_temperature}\n")
			print(f"Pressure:{self.pressure}\n")
			print(f"Humidity:{self.humidity}\n")
			print(f"Co-Ordinates:{self.co_ordinates}\n")
			print("\n")

			#Saving the datas in the text_file
			with open("weather_datas.txt","a") as f:
				self.sno=0
				f.write(f"S.No:{self.sno}\n")
				f.write(f"City_name:{self.city_name}\n")
				f.write(f"Weather_Description:{self.weather_description}\n")
				f.write(f"Current_Temperature:{self.current_temperature}\n")
				f.write(f"Pressure:{self.pressure}\n")
				f.write(f"Humidity:{self.humidity}\n")
				f.write(f"Co_Ordinates:{self.co_ordinates}\n\n\n")
				print("\n")
				print("{Weather details are copied in the text file successfully!")
				self.sno=self.sno+1

			#Saving the datas in the CSV format
			with open("weather_datas.csv",mode="a+") as f:
				fieldnames=["City_name","Weather_Description","Current_Temperature","Pressure","Humidity","Co_Ordinates"]	
				writer=csv.DictWriter(f,fieldnames)
				writer.writeheader()
				writer.writerow({"City_name":self.city_name,"Weather_Description":self.weather_description,"Current_Temperature":self.current_temperature,"Pressure":self.pressure,"Humidity":self.humidity,"Co_Ordinates":self.co_ordinates})
				print("CSV file created and copied datas successfully!}")
				print("\n")

		elif self.response.status_code == 429:
			print(f"Message:{self.response.status_code} Too many requests on these API's. Hence Blocked. Try again later!")

		elif self.response.status_code == 401:
			print(f"Message:{self.response.status_code}. Unauthorized access to this server via API. Please authenticate with your API in our Server! Thank You :)")

		else:
			print(f"City {self.city_name} is not found! Please check the spelling before you type in!")


# OpenWeatherMap API Key
API_KEY="a6e1bc1ceba3ef6ae534d88ce956b0cc"

# Base URL of the API
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

#datas instance for class WeatherMap()
details=WeatherMap("",API_KEY,BASE_URL,"","","","","","","","","","")
print(details.get_city_name())