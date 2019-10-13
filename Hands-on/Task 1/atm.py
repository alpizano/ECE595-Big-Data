amount = int(input("Enter the amount for withdrawal: "))

print(amount)

bill_100 = 100
bill_20 = 20
bill_5 = 5

count_100 = amount/bill_100
amount = amount % bill_100

count_20 = amount/bill_20
amount = amount % bill_20

count_5 = amount/bill_5
amount = amount % bill_5

print("Please collect your bills as follows:")
print("$%i: %i" % (bill_100,count_100))
print("$%i: %i" % (bill_20,count_20))
print("$%i: %i" % (bill_5,count_5))
