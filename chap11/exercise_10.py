#Sieve of Eratosthenes (finds prime numbers to range n)
def sieve(list):
    newList = []
    #take first item in list and announce as prime to initialize loop
    while len(list) != 0:
        newList.append(list[0])
        #remove multiples of that first number from the list
        #remove first number from the list
        try:
            for i in range(len(list)):
                if list[-i] % list[i] == 0:
                    list.remove(list[i])
        except:
            newList
    return newList 

def main():
    n = eval(input("Input value of n: "))
    list = [i+2 for i in range(n-1)]
    list = sieve(list)
    #no idea why 4 remains after iterating through this logic....but this seems to be a nice workaround
    # list.remove(2)
    # list.remove(4)
    print(list)

main()

