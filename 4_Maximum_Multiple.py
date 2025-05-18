divisor = int(input())
boundary = int(input())
N1 = 0

for N in range(1, boundary + 1, 1):
    if N % divisor == 0 and boundary >= N > 0:
        N1 = N
print(N1)
