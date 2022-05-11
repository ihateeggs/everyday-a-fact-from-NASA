import requests
import time
# import sys

dt = int(time.time())

url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=21.0278&lon=105.8342&dt={dt}&appid=13d6543b46227b1264e74645314147a5"

# original_stdout = sys.stdout  
response_ns = requests.get("https://api.nasa.gov/planetary/apod?api_key=ETNDm36Voef3ibJEg1RupywYcoIF86DfQx3vH58e")
response_wt = requests.get(url)

param_ns = response_ns.json() 
param_wt = response_wt.json()

ctemp = '%.2f' % (float(param_wt['current']['temp']) -273.15)

print (f"[{param_ns['date']}]")
print(f"Current temperature in Hanoi is: {ctemp} °C \n")
print (param_ns['explanation'])
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
