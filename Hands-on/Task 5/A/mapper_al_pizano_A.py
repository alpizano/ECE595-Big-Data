import sys
import read

for line in sys.stdin:
    line = line.strip()
	words = re.findall(r'\w+',line)
	
	for word in words:
	    print("{0: <20} 1".format(word.lower()))