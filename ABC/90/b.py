A, B = list(map(int, input().split()))
count = 0
for i in range(A, B+1):
    ii = int(str(i)[::-1])
    if i == ii:
        count += 1 
print(count)
