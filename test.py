a = eval(input('Enter a positive integer'))
b = eval(input('Enter a negative integer'))

print('The sum of all numbers are :', a + b)
print('The difference between the two numbers is :', a - b)
print('The multiplication between the two numbers is :', a*b)
print('The division between the two numbers is :' a/b)


x = -5
y = 1/(x+(1/(x+(1/(abs(x)+(1/x))))))
print("y =", y)

## B
hour = 12
minute = 17
dur = 2849

# nh = hour+((minute+dur)//60)
# if nh > 46: 
#     nh -=48
# if nh > 23: 
#     nh -=24
# print("nh =", nh)

# nm = minute + (dur%60) - 60
# print("nm =", nm)

endhour = hour + (dur // 60) 
endminute = minute + (dur % 60)
endhour += endminute // 60
endminute = endminute % 60
endhour = endhour % 24 

print(endhour, endminute)

def cal(x):  
    if x < 1582 : print('Not a Gregorian calendar year')
    if x > 1582:
        if x % 4 != 0 and x % 400 != 0:
            print("Common year")
        if x % 100 != 0 or x % 400 == 0:
            print("Leap year")
    
    
