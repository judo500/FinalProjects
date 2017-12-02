'''
Created on Dec 2, 2017

@author: ITAUser
'''
print("Enter file name to check:")
filename = input()

def calculate_char(filename, mychar):
    f = open(filename, 'r')
    count = 0
    isDone = False
    while not isDone:
        char=f.read(1)
        char=char.lower()
        if char==mychar:
            count+=1
        if char == '':
            isDone=True
    return(count)
import string

valueLetters = []
letters=list(string.ascii_lowercase)
for i in letters:
    a = calculate_char(filename, i)
    valueLetters.append(a)
pos = valueLetters.index(max(valueLetters))
mostCommon = letters[pos]
mostCommon = str(mostCommon)
print ("The most common letter in the file " + filename +" is " + mostCommon + " with a count of " + str(max(valueLetters)) + " occurences.")

#x = max(valueLetters)
#y = letters[x]
#print (y)