#!/usr/bin/python


class finder:
    memodict = None

    def __init__(self):
        self.memodict = {}

    def findall(self, target_char, string):
        keystring = "%s %s" % (target_char, string)
        if keystring in self.memodict.keys():
            return self.memodict[keystring]
        # given a target character and a string
        # return a list of all offsets (zero based) where the target character is found within the string
        positions = []
        curpos = 0
        for char in list(string):
            if char == target_char:
                positions.append(curpos)
            curpos += 1
        self.memodict[keystring] = positions
        return positions

def main(string):
    finder_obj = finder()
    pcount = 0
    for idx1 in range(len(string)-3):
        char1 = string[idx1]
        #print "starting with %s at %d" % (char1, idx1)
        others = finder_obj.findall(char1, string[idx1+3:])
        for raw_idx in others: 
            idx2 = raw_idx + idx1 + 3
            inner_string = string[idx1+1:idx2]
            #print "  found at %d as well" % (idx2)
            #print "  search substring %s" % (inner_string)

            for idx3 in range(len(inner_string)):
                tchar = inner_string[idx3]
                tothers = finder_obj.findall(tchar, inner_string[idx3+1:])
                for x in tothers:
                    pcount += 1

    return pcount
        
if __name__ == "__main__":
    string = raw_input().strip()
    answer = main(string)
    print (answer % (10**9 + 7) )
