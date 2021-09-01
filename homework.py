#1. Load the text data from the document, “AUGDAPData.txt” into your Python code
#2. Find a way to remove any non-numerical data from each line
#3. Make a list of the corrected data, in the same order as the original
#4. Create an output .txt file and save the data, separated 1 row per line, onto the file.

#C:\Users\Valentine0ne\Savvy Coders\coding\vamatrading-public



file1 = open("C:\\Users\\Valentine0ne\\Savvy Coders\\coding\\vamatrading-public\\AUGDAPData.txt", "r")

count = 0

with file1 as afile:
    afile = file1.readlines()
    for line in afile:
        count += 1
        print("line {}: {}".format(count, line.strip()))

