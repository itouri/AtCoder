N, K = list(map(int, input().split()))
count = 0
if K == 0:
    # N = pb + r
    # p = int(N/b)
    print(N*N)
    exit()
for i in range(1, N+1):
    count += int(N/i) * max(i-K, 0) + max(N - int(N/i)*i + 1 - K, 0)
print(count)