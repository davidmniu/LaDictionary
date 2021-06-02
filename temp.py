import re

file = open("dictionary.tex", "r")
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    line = line.strip()
    if (line[1:6] == "entry"):
        #print(line)
        print(re.split(r"\\entry{|}", line, 3)[1])
 
file.close()
