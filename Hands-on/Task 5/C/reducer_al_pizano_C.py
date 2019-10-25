import sys

prev_host = None
count = 1

for line in sys.stdin:
    line = line.strip()
    line = line.split()

    # If key is equal to last key, then increase count+1
    if line[0] == prev_host:
        count = count+1

    # Else print the key and count to stdout
    else:
        if prev_host is not None:
            print("{0: <30} {1:}".format(prev_host,count))
        count = 1
        prev_host = line[0]

print("{0: <30} {1:}".format(prev_host,count))

