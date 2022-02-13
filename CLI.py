from datetime import datetime
import json
from turtle import color
import requests
import sys
import numpy as np
import matplotlib.pyplot as plt

#fetch data from the API and returns it
def fetchData():
    #variable for checking formart
    format= "%d-%m-%Y"
    #loop until correct format is entered
    var1=''
    var2=''
    while(1):
        #allow user to enter args
        start= input("Enter a start date to filter from: ")
        end=input("Enter a end date to filter to: ")
        try:
            #check if is correct format the breaks if not
            datetime.strptime(start, format)
            datetime.strptime(end, format)
            var1=start
            var2=end
            break
        except:
            print("This is the incorrect date string format. It should be dd-mm-yyyy")
        
    try:
        #connect to the API
        response=requests.get('http://sam-user-activity.eu-west-1.elasticbeanstalk.com/')
        #get data from the API
        data=response.text
        #convert data to json format
        json_data = json.loads(data)
        #loop through the data and check to filter the dates
        for key in list(json_data):
            if(key<var1 or key>var2):
                del json_data[key]
        #return the filtered data
        return json_data
    except :
        print('Cant connect to the API')
        sys.exit(1)

#draw barGraphs
def drawGraph(data):
    #changes data to list
    dates = list(data.keys())
    users = list(data.values())
    if(len(dates)>0):
        fig = plt.figure(figsize= (10,7))
        #set color to blue and width to 0.7 
        plt.bar(dates, users ,color ='blue', width=0.7)
        #label and plot the graph
        plt.xlabel("Dates")
        plt.ylabel("Number of active users")
        plt.title("BarGraph for active user per given dates")
        plt.show()
    else:
        print("No data to shows")

if __name__ == "__main__":
    print("Dates should be in formart dd-mm-yyyy")
    drawGraph(fetchData())