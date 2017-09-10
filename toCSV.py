#imports
import os

#methods
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def diff(s1, s2):
    one = []
    two = []
    for c1 in s1:
        if c1 not in s2:
            one.append(c1)
    for c2 in s2:
        if c2 not in s1:
            two.append(c2)
    return [one, two]

def toCSV(rawName, toName):
    file = open(rawName + ".txt", "r")
    out = open(toName + ".csv", "wb")
    temp = "0"

    values = file.readlines()
    t = []

    for e in values:
        for i in e.split(" "):
            t.append(i)

    values = t

    out.write(("0,0, Header,1,3,384,\n1,0, Start_track,,,,\n1,0, Time_signature,4,2,24,8\n1,0, Tempo,500000,,,\n1,"+ """length of the track""" + ", End_track,,,,\n").encode("utf-8"))
    out.write(("2,0, Start_track,,,,\n2,0, Text_t,\"\"\"harpsichord: John Sankey\"\"\"\,,,\n2,0, Title_t,\" \"\"Track 1\"\"\",,,").encode("utf-8"))

    for i in range(len(values)):
        if values[i] != temp:
        #compute string distance/differences
            remove, add = diff(temp, values[i])
            for e in ''.join(set(add)):
                out.write(("2," + str(i) + ", Note_on_c,0," + str(ord(e)) + ",127,\n").encode("utf-8"))
            for e in ''.join(set(remove)):
                out.write(("2," + str(i) + ", Note_off_c,0," + str(ord(e)) + ",127,\n").encode("utf-8"))
            temp = values[i]

    out.write(("2,"+ str(len(values)+9) + ", End_track,,,,\n3,0, Start_track,,,,\n3,0, Title_t,\" \"\"MIDI\"\"\",,,\n3,1536, End_track,,,,\n0,0, End_of_file,,,,").encode("utf-8"))

    out.close()
        
