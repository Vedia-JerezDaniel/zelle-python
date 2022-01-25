#This program accepts a sequence of average daily temps and computes
#the running total of cooling and heating degree days
def main():
    avgTemp = 0
    coolDeg = 0
    heatDeg = 0
    while True:
        avgTemp = input("Enter average daily temperature (Type 'Exit' to quit)>> ")
        if avgTemp.lower() == "exit":
            break
        try:
            avgTemp = int(avgTemp)

            if avgTemp < 60:
                coolDeg += abs((avgTemp - 60))
            elif avgTemp > 80:
                heatDeg += avgTemp - 80
            else:
                avgTemp = avgTemp
        except (ValueError, IndexError):    
            print("Make sure your input is a number.")
    print("The cooling degree-day is {0} and the heating degree-day is {1}".format(coolDeg, heatDeg))

main()
