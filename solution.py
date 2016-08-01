#!/usr/bin/python


def findall(target_char, string):
    # given a target character and a string
    # return a list of all offsets (zero based) where the target character is found within the string
    positions = []
    curpos = 0
    for char in list(string):
        if char == target_char:
            positions.append(curpos)
        curpos += 1
    return positions

def main(string):
    for idx1 in range(len(string)-3):
        char1 = string[idx1]
        print "starting with %s at %d" % (char1, idx1)
        others = findall(char1, string[idx1+3:])
        for idx2 in others: 
            print "  found at %d as well" % (idx1 + idx2 + 3)
        
if __name__ == "__main__":
    string = raw_input().strip()
    print string
    main(string)
