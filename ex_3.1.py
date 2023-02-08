
hrs = input('How many hours have you worked?')
rate = input('What is the rate?')

h = float(hrs)
r = float(rate)

normalpay = (h * r)
overpay = ((h - 40) * 1.5 * r) + (40 * 10.5)
if h < 40:
    print(h * r)
else:
    print(overpay)



