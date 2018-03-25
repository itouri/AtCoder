
N, Y = list(map(int, input().split()))
 
a = Y // 10000
b = (Y - a * 10000) // 5000
c = (Y - a * 10000 - b * 5000) // 1000

ary = [] 

while 1:
    print(a, b, c)
    t = a + b + c
    if N >= t + 9 and a > 0:
        a -= 1
        c += 10
        continue
    if N >= t + 4 and b > 0:
        b -= 1
        c += 5
        continue
    if N > t and a > 0:
        a -= 1
        b += 2
        continue
    break
 
if a + b + c != N or a < 0 or b < 0 or c < 0:
    print("-1 -1 -1")
else:
    print(a, b, c)