linlst = []

infile = open("C:\\Users\\Valentine0ne\\Savvy Coders\\Coding\\vamatrading-public\\importtext.txt")

aline = infile.readline()
while aline:
    aline = infile.readline()
    linlst.append(aline)

infile.close()

print(linlst)
