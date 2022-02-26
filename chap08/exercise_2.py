# Get into the habit of using more descriptive variable names.
# It will make the lives of whoever has to read this code easier (yourself included)
def windchill(temperature, windspeed):
    return (
        35.74
        + (0.6215 * temperature)
        - (35.75 * (windspeed ** 0.16))
        + (0.4275 * temperature) * (windspeed ** 0.16)
        if 50 >= windspeed >= 3
        else 0
    )

def generateWindchillTable(rows):
    """Extra credit - find a way to ensure the rows argument is a number, 
    and not a string or a boolean (the for loop will fail if it isn't)
    """  
    try:
        if rows == True or rows == False or rows is None:
            print("Not a number")
        else:
            val = {-20,-10,0,10,20,30,40,50,60,70}
            for i in range (rows):
                for v in val:
                    print(i,'> wind >',v,' : ',"{:>5.1f}:".format(i*windchill(v, i*5)))
    except (NameError, TypeError) as rows:
        print('rows must be a number!')
    except SyntaxError:
        print("rows must be a number!")



generateWindchillTable(11)

