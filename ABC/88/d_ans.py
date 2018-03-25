H, W = map(int, input().split())
s = [input() for _ in range(H)]
dic = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = [[0, 0, 0]]
distances = [[float('inf') for i in range(W)] for j in range(H)]
distances[0][0] = 0
ans = H * W
black = 0
for ss in s:
    black += ss.count('#')
while len(queue) > 0:
    #n = queue.pop()
    n = queue[0]
    queue = queue[:0]
    for d in dic:               
        nx = n[0] + d[0]
        ny = n[1] + d[1]
        if nx < 0 or W <= nx or ny < 0 or H <= ny:
            continue 
        if nx == W-1 and ny == H-1:
            ans = min(distances[n[1]][n[0]] + 1, ans)
        elif s[ny][nx] == "." and distances[ny][nx] > distances[n[1]][n[0]] + 1:
            distances[ny][nx] = distances[n[1]][n[0]] + 1
            queue.append([nx, ny])
print(-1 if ans == H*W else H*W - (ans+1) - black)