N, M = list(map(int, input().split()))
if N * M == 1:
    print(1)
elif N == 1 or M == 1:
    if N == 1:
        print(M-2)
    if M == 1:
        print(N-2)
elif N == 2 or M == 2 :
    print(0)
else:
    print((N-2)*(M-2))