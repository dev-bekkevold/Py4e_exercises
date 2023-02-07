
h = float(input('How many hours have you worked?'))
r = float(input('What is the rate?'))

normalpay = (h * r)
overpay = ((h - 40) * 1.5 * r) + (40 * 10.5)
if h < 40:
    print(h * r)
else:
    print(overpay)



