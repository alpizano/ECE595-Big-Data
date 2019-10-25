import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    city = line[2]
    sales = line[4]

    print("{0: <20} {1:}".format(city,sales))
