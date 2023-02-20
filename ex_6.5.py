
text = "X-DSPAM-Confidence:    0.8475"

num = text.find('0')
# print(num)
code = (text[num-1:])
print(float(code))

