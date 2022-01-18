def toNumbers(strList):
    for x in range (len(strList)):
        strList[x] = int(strList[x])
    return(strList)

def squareEach(nums):
    for x in range (len(nums)):
        nums[x] = nums[x] ** 2
    return(nums)

def sumList(nums):
    y = 0
    for x in range (len(nums)):
        y = nums[x] + y
    return(y)

def main():
    fname = input("Enter filename: ")
    with open(fname, "r") as infile:
        lines = list(infile.readlines())
        x = toNumbers(lines)
        y = squareEach(x)
        z = sumList(y)
        print(z)
main()
