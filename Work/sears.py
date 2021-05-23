#
#sears.py

bill_thickness = 0.11 * 0.001 # convert to meters
sears_height = 442 #height in m

num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)