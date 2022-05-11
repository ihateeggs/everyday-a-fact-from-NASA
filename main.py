import requests
import sys

original_stdout = sys.stdout  
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=ETNDm36Voef3ibJEg1RupywYcoIF86DfQx3vH58e")

param = response.json() 
 
# with open('demo.txt', 'w') as f:
#     sys.stdout = f 
#     print (param['date'] + "\n")
#     print (param['explanation'])
#     print("\n")
#     print("Here is link of" + param['title'] + ": " + param['url'])
#     # Reset the standard output
#     sys.stdout = original_stdout

# print("The information has already in the demo.txt file")

print (f"[{param['date']}]" + "\n")
print (param['explanation'])
print("\n")
print(f"Here is link of {param['title']}: {param['url']} \n")
print("Have a nice day!!!")