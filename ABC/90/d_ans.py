N, K = list(map(int, input().split()))
t = [(i-K)*(N//i) + max(N-(N//i)*i+1-K, 0) for i in range(K+1, N+1)]
print(sum(t))