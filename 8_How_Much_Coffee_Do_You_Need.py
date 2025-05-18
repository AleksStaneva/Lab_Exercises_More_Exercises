coffee_cups = 0

while True:
    command = input()

    if command == "END":
        break

    if command != "coding" and command != "dog" and command != "cat" and command != "movie" and command != "CODING" and command != "DOG" and command != "CAT" and command != "MOVIE":
        continue

    if command and command[0].isupper():
        coffee_cups += 2
    elif command and command[0].islower():
        coffee_cups += 1

    if coffee_cups > 5:
        print(f"You need extra sleep")
        break

if coffee_cups <= 5:
    print(coffee_cups)