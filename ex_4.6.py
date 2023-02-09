# How to use functions with userinput

hrs = input('How many hours have you worked?')
rate = input('What is the rate?')

h = float(hrs)
r = float(rate)

def computepay(h, r):
    if h < 40:
        print(h * r)
    return ((h - 40) * 1.5 * r) + (40 * r)

p = computepay(h, r)
print("Pay", p)

