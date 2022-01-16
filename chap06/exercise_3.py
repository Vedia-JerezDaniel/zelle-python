import math

def main():
    r = (eval(input("Input a value for the radius: ")))
    a = 4 * math.pi * (r**2)
    v = 4/3 * math.pi * (r ** 3)
    print("A sphere with radius", r, "has volume", round(v, 3), "and surface area", round(a, 3),".")

main()

