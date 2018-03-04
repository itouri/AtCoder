import functools

N = int(input())
march = ["M","A","R","C","H"]
S = {}
for m in march:
    S[m] = 0

for i in range(N):
    s = input()
    if s[0] in march:
        S[s[0]] += 1

aS = [s for s in S.values() if s != 0]

mul = functools.reduce(lambda a, x: a * x, aS, 1)
ans = 0
if len(aS) == 3:
    ans = mul
elif len(aS) == 4:
    ans = functools.reduce(lambda a, x: a + mul/x, aS, 0)
elif len(aS) == 5:
    for i in range(5):
        for j in range(i+1,5):
            ans = ans + mul / aS[i] / aS[j]
print(int(ans))