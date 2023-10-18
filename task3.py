#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def find():
    filename = 'task03.txt'
    file = open(filename,'r')
    datalist = file.read().split('\n')
    for i in datalist:
        
        listsplit = i.split(' ')
        listsplit.sort()
        i = int(i)
        
find()