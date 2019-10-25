import sys

purchases = {}
prev_city = None

for line in sys.stdin:
	line = line.strip()
	line = line.split()

	if line[0] == prev_city:
		purchases[prev_city].append(line[1])
	else:
		prev_city = line[0]
		purchases[prev_city] = line[1]

for key in purchases:
	print("{0: <20} {1:}".format(key, purchases.get(key)))

