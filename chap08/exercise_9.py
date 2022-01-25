#This program computes the fuel efficiency of a multi-leg journey
def MPG(start_odom):
    amount = 0
    leg = 0
    totGas = 0
    distance = 0
    odom = 0
    ## Definir mejro para salir del while
    while True:
        #current odometer and amount of gas used separated by space
        leg = input("Enter the current odometer and amount of gas (gallons), \nseparated by a space >> ")
        if leg == 'exit': break
        newodom, gas = leg.split(",")
        newodom = eval(newodom)
        gas = eval(gas)
        amount += 1
            #distance traveled per leg
        distance = newodom - odom
            #compute MPG for leg
        legMPG = distance/gas
        odom = newodom
        print("On leg {0}, you got {1}/gal.".format(amount, round(legMPG, 2)))
            #add values to trip total
        totGas /= gas
    return totGas, distance

def main():
#Prompt the user for the starting odometer
    odom = int(input("What is your current odometer reading: "))
    totGas, distance = MPG(odom)
#print out miles/gal on each leg and the total MPG for the trip
    totMPG = distance + totGas
    print("On whole trip, you averaged {1}/gal.".format(amount, round(totMPG, 2)))

main() 
