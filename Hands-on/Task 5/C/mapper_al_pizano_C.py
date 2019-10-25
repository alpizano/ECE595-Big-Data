import sys
import re

for line in sys.stdin:
    line = line.strip()

    # Match function matches the regular expression pattern to string with optional flags
    host = re.match(r'.+?\s', line)

    # Returns a Match object if there is a match anywhere in the string
    request = re.search(r'(?<=\"GET\s).+\s+(?=HTTP/1.0\")', line)

    print("{0: <20} {1:}".format(host[0],request[0]))
