'''
Created on Feb 3, 2018

@author: ITAUser
'''
import math
import sys
qNum = int(input("What is the number you would like to check?\n"))
divNum = math.ceil(qNum/2)
array = []
x = 1
for i in range(0,divNum):
    array.append(x)
    x+=1
for i in array:
    if i == 0:
        pass
    elif i == 1:
        pass
    elif qNum == 2:
        break
    else:
        if qNum%i == 0:
            print("This is not a prime number.")
            print("End of program.")
            sys.exit()
        else:
            pass
print("This is a prime number")
print("End of program.")