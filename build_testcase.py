import random
import sys

length = 100
if len(sys.argv) > 1:
    try:
        length = int(sys.argv[1])
    except:
        pass

charset = ['a','b','c','d','e','f','g','h','i']

string_array = []
for x in range(length):
    string_array.append(random.choice(charset))
print "".join(string_array)

