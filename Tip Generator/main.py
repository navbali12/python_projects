# welcome message

print('HYE! I am a tip calculator!')

b=input("What was the total bill? \n$ ")
t=input("How much tip would you like to give? 10, 12, or 15? \n " )
p=input("How many people to split the bill?")

bill=float(b)
tip=float(t)
people=float(p)

#logic for finding tip and rounding to two decimal places
total=round(((bill*(tip/100)+bill)/people),2)


print(f"Each person should pay:${total}")
print("thank you")
