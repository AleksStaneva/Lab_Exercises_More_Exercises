n = int(input())

for _ in range(n):
    command = input()
    if "," in command or "." in command or "_" in command:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")