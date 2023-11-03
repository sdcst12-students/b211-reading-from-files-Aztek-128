"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

#hasga;kghas;jhaefkjgadkjvbaekbadkf;jvneaibadkvbeaivbaeivbaebaepivbeaibalvkjaebviaefjbvafibvepivbadlvjebq;lijdabcvk;jebiefoveiafjvbad;ivbqeiubdkfvbad;liubiadfjbvaekl;jvbae;ibadvbeai;vbad;ivbeai;vubadk;vjbaeijvbeaivbdackjvabeiv;aeubv;iajvbeaibaldi
symbol = input("enter stock symbol: ").upper()
filename = 'task5.csv'
symbolamount = 0
file = open(filename, 'r')
read = file.read().split("\n")
stocklist = []
for i in read:
    #for o in stocklist:
    if symbol in i:
        stocklist.append(i)
        symbolamount += 1
    else:
        pass
print(f"the amount of companys with this stock name is {symbolamount}")
symbol2 = input("enter stock symbol: ").upper()
for o in stocklist:
    if symbol2 in o:
        print(f"this is your company {o}")


