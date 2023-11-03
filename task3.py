#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def find(x = None):
    filename = 'task03.txt'
    file = open(filename,'r')
    totallist = []
    datalist = file.read().split('\n')
    total = 0
    for i in datalist:
        try:
            i = int(i)
            total += i
        except:
            totallist.append(total)
            total = 0
    totallist.sort()
    print(totallist[-1])
        
find()