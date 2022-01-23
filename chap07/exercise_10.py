def Easter(year):
    
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        print(a, b, c, d, e)
        if (d + e) > 9:
            print("Easter falls on April {}.".format(d + e - 9))
        else:
            print("Easter falls on March {}.".format(22 + d + e))
        if year == 1954 | year == 1981 |year == 2049 | year == 2076:
            if (d + e) > 9:
                d = d - 7
                print("Easter falls on April {}.".format(d + e - 9))
            else:
                d = d - 7
                print("Easter falls on March {}.".format(22 + d + e))
    else:
        print("Year is out of range")


Easter(1981)
Easter(1982)
