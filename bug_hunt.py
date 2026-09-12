
count = 1
total = 0

# BUG: The while statement was missing a colon, so I added one.
# BUG: The condition stopped before adding 5, so I changed count < 5 to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The total is an integer, so I converted it to a string before joining it with the message.
print("Sum of 1 to 5 is: " + str(total))
