customer_name = input("Enter customer name: ")
tickets = int(input("Enter number of tickets: "))

ticket_price = 200
total_amount = tickets * ticket_price

if tickets > 5:
    print("give 10% discount")
    discount = total_amount * 0.10
    print("Discount=",discount)
    total_amount = total_amount - discount

print("Customer Name:", customer_name)
print("Number of Tickets:", tickets)
print("Final Amount: ₹", total_amount)