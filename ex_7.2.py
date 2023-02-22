# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                num = num + float(line[20:])
                count = count + 1

print("Average spam confidence:", num/count)




