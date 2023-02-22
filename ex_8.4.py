# use the file "romeo.txt"

fname = input("Enter file name: ")
fh = open(fname)
text = []

for line in fh:
    words = line.split()
    for line in words:
        if line not in text:
            text.append(line)
print(sorted(text))
    