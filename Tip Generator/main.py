# welcome message

print('Welcome to the tip calculator!')

b=input("What was the total bill?")
t=input("How much tip would you like to give? 10, 12, or 15?")
p=input("How many people to split the bill?")

bill=int(b)
tip=int(t)
people=int(p)

#logic for finding tip
total=bill*(tip/100)+bill

print(f"Each person should pay:${total}")
