#(a) count(myList,  x)  (like myList.count(x))
def count(myList, x):
    return sum(i == x for i in myList)

#(b) isin(myList, x)    (like x in myList)
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

#(c) index(myList, x)   (like myList.index(x))
def index(myList, x):
    for i in range (len(myList)):
        if myList[i] == x:
            return i

#(d) reverse(myList)    (like myList.revers())
def reverse(myList):
    return [myList[-1 * (i + 1)] for i in range(len(myList))]

#(e) sort(myList)       (like myList.sort())
def sort(myList):
    newList = []
    for _ in range (len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList

        
def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    myList *= 3
    x = 3
    print("Count of x: ", count(myList, x))
    print("X in myList: ", isin(myList, x))
    print("Index of x: ", index(myList, x))
    print("Reverse list: ", reverse(myList))
    print("Sort List: ", sort(myList))


main()

myList = [8, 6, 7, 5, 3, 0, 9]

for i in range(len(myList)):
    myList[-1 * (i + 1)] 

myList[-2]

