"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def find():
    #MyList = []
    filename = 'task02a.txt'
    file = open(filename,'r')
    data = file.read()
    datalist = data.split('\n\n')
    #count = 0
    for i in datalist:
        listsplit = i.split('\n')
        listsplit.sort()
        print(listsplit)
        try:
            if ((float(listsplit[0]))**2) + ((float(listsplit[1]))**2) == ((float(listsplit[2]))**2):
                print("yeah")
        except:
            pass
            


find()