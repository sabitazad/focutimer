import time
import os 

os.system('color B')
duration = int(input("Enter the amount of time (in seconds) you want to focus: "))

while duration:
    try:
      mins, secs = divmod(duration, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")
      time.sleep(1)
      duration -= 1
    except ValueError:
            print()
            print("Please input a valid number")
            print() 
    continue
os.system('color 6')

print()
input("You've made it!")
