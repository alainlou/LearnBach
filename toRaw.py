file = open("846.csv" , "r")

out = open("output.txt", "wb")

end = 0

while True:
    line = file.readline()
    if not line:
        break
    else:
        if "End_track" in line:
            end = int(line.split(",")[1])
            break

terms = [" "] * end

lines = [i.split(",") for i in file.readlines()]

for i in range(21, 109):
    for j in range(len(lines)):
        if lines[j][4] and int(lines[j][4]) == i+1 and "Note_on" in lines[j][2]:
            for k in range(j+1, len(lines)):
                if lines[k][4] and int(lines[k][4]) == i+1 and "Note_off" in lines[k][2]:
                    for l in range(int(lines[j][1]),int(lines[k][1])):
                        terms[l] += str(chr(i))
                    break


for term in terms:
    out.write(term.encode("ascii"))
    
file.close()
