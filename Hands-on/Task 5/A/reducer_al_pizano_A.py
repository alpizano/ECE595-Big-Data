import sys

# reduces and retrieves Top 10

dict = {}

for line in sys.stdin:
    values = line.split()
	if values[0] in dict:
	    count = dict.get(values[0])
		count = count+1
		dict[values[0]] = count
	else:
	    dict[values[0]] = int(values[1])
		
for key in sorted(dict, key=dict.get, reverse=True)[:10]:
    print("%s %s" % (key,dict[key]))