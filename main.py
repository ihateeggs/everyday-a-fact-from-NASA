import requests
# import sys
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

key = "13d6543b46227b1264e74645314147a5"
lat = 21.027
lon = 105.8342
dt = int(time.time())

url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={key}"

# original_stdout = sys.stdout  
response_ns = requests.get("https://api.nasa.gov/planetary/apod?api_key=ETNDm36Voef3ibJEg1RupywYcoIF86DfQx3vH58e")
response_wt = requests.get(url)

param_ns = response_ns.json() 
param_wt = response_wt.json()

ctemp = '%.2f' % (float(param_wt['current']['temp']) -273.15)
ftemp = '%.2f' % (float(param_wt['current']['feels_like']) -273.15)

crw = param_wt['current']['weather'][0]



#Print stuff here
print (f"[{param_ns['date']} - {current_time}({param_wt['timezone']})]")

#WEATHER:
print(f"\nCurrent temperature in Hanoi is: {ctemp}°C & Feel like {ftemp}°C")
print(f"The weather now: {crw['description']}\n")

#NASA
print (f"Now to the fact of the day:\n{param_ns['explanation']}\n")
print(f"Here is link of {param_ns['title']}'s {param_ns['media_type']} : {param_ns['url']} \n")
print("Have a nice day!!!")


# with open('demo.txt', 'w') as f:
#     sys.stdout = f 
#     print (f"[{param_ns['date']} - {current_time}]")
#     print(f"\nCurrent temperature in Hanoi is: {ctemp}°C & Feel like {ftemp}°C")
#     print(f"The weather now: {crw['description']}\n")
#     print (f"Now to the fact of the day:\n{param_ns['explanation']}\n")
#     print(f"Here is link of {param_ns['title']}: {param_ns['url']} \n")
#     print("Have a nice day!!!")
#     # Reset the standard output
#     sys.stdout = original_stdout
#
# print("The information has already in the demo.txt file")
