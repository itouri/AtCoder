import itertools
N, K = list(map(int, input().split()))
count = 0
for i in range(K, N+1):
    count += N - i
    # ount += int(i/2) - K
    # if i % 2 == 1:
    #     count += 1
for i in range(K+1, N+1):
    for j in range(1, i):
    # for j in range(1, int(i/2)+1):
        if i % j >= K:
            count += 1
print(count)