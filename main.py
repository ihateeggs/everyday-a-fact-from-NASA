import requests
# import sys
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

dt = int(time.time())

url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=21.0278&lon=105.8342&dt={dt}&appid=13d6543b46227b1264e74645314147a5"

# original_stdout = sys.stdout  
response_ns = requests.get("https://api.nasa.gov/planetary/apod?api_key=ETNDm36Voef3ibJEg1RupywYcoIF86DfQx3vH58e")
response_wt = requests.get(url)

param_ns = response_ns.json() 
param_wt = response_wt.json()

ctemp = '%.2f' % (float(param_wt['current']['temp']) -273.15)
ftemp = '%.2f' % (float(param_wt['current']['feels_like']) -273.15)

crw = param_wt['current']['weather'][0]



#Print stuff here
print (f"[{param_ns['date']} - {current_time}]")

#WEATHER:
print(f"\nCurrent temperature in Hanoi is: {ctemp}°C & Feel like {ftemp}°C")
print(f"The weather now: {crw['description']}\n")

#NASA
print (f"Now to the fact of the day:\n{param_ns['explanation']}")
print("\n")
print(f"Here is link of {param_ns['title']}: {param_ns['url']} \n")
print("Have a nice day!!!")


# with open('demo.txt', 'w') as f:
#     sys.stdout = f 
#     print (param['date'] + "\n")
#     print (param['explanation'])
#     print("\n")
#     print("Here is link of" + param['title'] + ": " + param['url'])
#     # Reset the standard output
#     sys.stdout = original_stdout

# print("The information has already in the demo.txt file")
