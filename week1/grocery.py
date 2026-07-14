items = {
    "rice": 100,
    "sugar": 80,
    "wheat": 60,
    "oil": 150
}

total_bill = 0

while True:
    item = input("Enter your item: ")
    quantity = int(input("Enter quantity: "))

    if item in items:
        total_bill += items[item] * quantity   
    else:
        print("Item is not available")

    choice = input("Add another item (yes/no): ")
    if choice != "yes":
        break

if total_bill > 500:
    discount = total_bill * 0.10
else:
    discount = 0

final_amount = total_bill - discount


print("\nTotal Bill =", total_bill)
print("Discount =", discount)
print("Final Amount =", final_amount)