linlst = []

infile = open("C:\\Users\\mysti\\Coding\\Prose_Dream.txt", "r")

aline = infile.readline()
while aline:
    try:
        aline = infile.readline()
        linlst.append(aline)

    except:
        print("Input error.")

infile.close()

print(linlst)
