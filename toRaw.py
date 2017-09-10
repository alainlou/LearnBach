def toRaw(filename, outname, transpose):
    file = open(str(filename) + ".csv" , "r")

    out = open(str(outname) + ".txt", "ab")

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
            if len(lines[j])>4 and lines[j][4] and int(lines[j][4]) == i+1 and "Note_on" in lines[j][2]:
                for k in range(j+1, len(lines)):
                    if lines[k][4] and int(lines[k][4]) == i+1 and "Note_off" in lines[k][2]:
                        for l in range(int(lines[j][1]),int(lines[k][1])):
                            terms[l] += str(chr(i+transpose))
                        break


    for term in terms:
        out.write(term.encode("ascii"))

    out.write(("                                                  ").encode("ascii"))

    out.close()
