def baseConversion(num, base):
    digit = num % base
    num = num // base
    print(num, digit)
    
    if num == 0:
        return 1
    elif num < base:
        digit = num
        num = 0
    else:
        baseConversion(num, base)
    
baseConversion(245, 16)

        

