#This program accepts a sequence of average daily temps and computes
#the running total of cooling and heating degree days
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    coolDeg = 0
    heatDeg = 0
    avgTemp = 1
    while avgTemp != None:
        for avgTemp in infile.readlines():
            print(avgTemp)
            try:
                avgTemp = int(avgTemp[:-1])
                if avgTemp < 60:
                    coolDeg += abs((avgTemp - 60))
                elif avgTemp > 80:
                    heatDeg += avgTemp - 80
                else: avgTemp = avgTemp
            except ValueError:
                if avgTemp[:-1] == ' ': break
                else: return False
            finally:
                infile.close()
        break
    print("The cooling degree-day is {0} and the heating degree-day is {1}.".format(coolDeg, heatDeg))


main()
