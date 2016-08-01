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
    pcount = 0
    for idx1 in range(len(string)-3):
        char1 = string[idx1]
        #print "starting with %s at %d" % (char1, idx1)
        others = findall(char1, string[idx1+3:])
        for raw_idx in others: 
            idx2 = raw_idx + idx1 + 3
            inner_string = string[idx1+1:idx2]
            #print "  found at %d as well" % (idx2)
            #print "  search substring %s" % (inner_string)

            for idx3 in range(len(inner_string)):
                tchar = inner_string[idx3]
                tothers = findall(tchar, inner_string[idx3+1:])
                for x in tothers:
                    pcount += 1

    return pcount
        
if __name__ == "__main__":
    string = raw_input().strip()
    answer = main(string)
    print (answer % (10**9 + 7) )
