def removeDuplicates(myList):
    newList = []
    for i in myList:
        if i not in newList:
            newList.append(i)
    return newList

def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    myList *= 3
    print("Remove Duplicate: ", removeDuplicates(myList))


main()

