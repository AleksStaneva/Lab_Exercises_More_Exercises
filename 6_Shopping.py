budget = int(input())
command = input()
total_price = 0

while command != "End":

    product_price = int(command)
    total_price += product_price

    if total_price > budget:
        print("You went in overdraft!")
        break

    command = input()

if total_price <= budget:
    print("You bought everything needed.")

