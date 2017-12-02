'''
Created on Nov 18, 2017

@author: ITAUser
'''
print("Enter file name to check:")
filename = input()

print("Enter the character you would like to examine:")
x = input()

rep = open(filename, "r").read()
    
words = rep.split()
spaces = len(words)-1
countChar = 0
count1 = 0
count2 = 0

for w in words:
    for y in w:
        if y == x:
            countChar += 1
        elif y == x.lower():
            countChar += 1
        elif y == x.upper():
            countChar += 1
print ("Number of " + x + "'s in the file: " + str(countChar))