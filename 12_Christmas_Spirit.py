decoration_quantity = int(input())
days_until_Christmas = int(input())

money_spent = 0
christmas_spirit = 0
going_shopping_counter = 0
budget = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_spirit = 5
tree_skirt_spirit = 3
tree_garland_spirit = 10
tree_lights_spirit = 17

for day in range(1, days_until_Christmas + 1):

    if day % 11 == 0:
        decoration_quantity += 2

    if day % 2 == 0:
        budget += ornament_set_price * decoration_quantity
        total_spirit += ornament_set_spirit

    if day % 3 == 0:
        budget += (tree_skirt_price + tree_garland_price) * decoration_quantity
        total_spirit += tree_skirt_spirit + tree_garland_spirit

    if day % 5 == 0:
        budget += tree_lights_price * decoration_quantity
        total_spirit += tree_lights_spirit
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt_price + tree_garland_price + tree_lights_price

if days_until_Christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")






