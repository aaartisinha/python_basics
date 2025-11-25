#SHOPPING BILL CALCULATOR

print("shopping bill calculator")

num_items = int(input("Enter number of items: "))

total = 0

for i in range(1,num_items + 1):
    price = float(input(f"Enter price of item{i}: "))
    total += price 
    
print ("Total Bill Amount =", total)
