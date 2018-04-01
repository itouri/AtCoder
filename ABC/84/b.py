import re
ab = list(map(int, input().split()))
S = input()
if S[ab[0]] != '-':
    print("No")
    exit()

s = S.split('-')
if len(s) > 2:
    print("No")
    exit()

for i in range(2):
    if not ( len(s[i]) == ab[i] and re.compile(r'\d').match(s[i]) ):
        print("No")
        exit()
print("Yes")