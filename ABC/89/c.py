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

aS = []
for s in S.values():
    if s != 0:
        aS.append(s)

mul = 1
ans = 0
sum = 0
for s in aS:
    mul = mul * s
    sum += 1
if sum == 3:
    ans = mul
elif sum == 4:
    # ans = mul * 4
    for s in aS:
        ans = ans + mul / s
elif sum == 5:
    # ans = mul * 5
    for i in range(5):
        for j in range(i+1,5):
            ans = ans + mul / aS[i] / aS[j]
print(int(ans))