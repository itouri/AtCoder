N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
t = [sum(A[0][:i])+sum(A[1][i-1:]) for i in range(N+1)]
print(max(t))
