def main():
    myList = [8,6,7,5,3,0,9]
    newList = [9,0,3,5,7,6,8]

    result = sum(myList[i] * newList[i] for i in range(len(myList)))
    print(result)
    
    
main()