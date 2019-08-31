import fileinput

for line in fileinput.input("TextFile.dat"):
    print(line,end='')
