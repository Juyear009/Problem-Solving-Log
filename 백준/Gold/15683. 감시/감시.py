N,M = map(int,input().split())
graph = []
cctv = []

def check(x,y,dx,dy,t):
  while True:
    x += dx
    y += dy
    if 0 <= x < N and 0 <= y < M:
      if graph[x][y] == 0:
        if t == "add":
          cnt[x][y] += 1
        else:
          cnt[x][y] -= 1
      elif graph[x][y] == 6:
        break
    else:
      break

def recursion(n):
  global answer
  if n == len(cctv):
    temp = 0
    for i in range(N):
      for j in range(M):
        if graph[i][j] == 0 and cnt[i][j] == 0:
          temp += 1
    if answer > temp:
      answer = temp
    return
  
  x,y,t = cctv[n]
  if t == 1:
    for dx,dy in d:
      check(x,y,dx,dy,"add")
      recursion(n+1)
      check(x,y,dx,dy,"delete")
  elif t == 2:
    for i in range(2):
      for j in [i,i+2]:
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"add")
      recursion(n+1)
      for j in [i,i+2]:
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"delete")
  elif t == 3:
    for i in range(4):
      for j in range(i,i+2):
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"add")
      recursion(n+1)
      for j in range(i,i+2):
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"delete")
  elif t == 4:
    for i in range(4):
      for j in range(i,i+3):
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"add")
      recursion(n+1)
      for j in range(i,i+3):
        dx = d[j%4][0]
        dy = d[j%4][1]
        check(x,y,dx,dy,"delete")
  elif t == 5:
    for dx,dy in d:
      check(x,y,dx,dy,"add")
    recursion(n+1)
    for dx,dy in d:
      check(x,y,dx,dy,"delete")



for i in range(N):
  temp = list(map(int,input().split()))
  graph.append(temp)
  for j in range(M):
    if temp[j] in [1,2,3,4,5]:
      cctv.append([i,j,temp[j]])

answer = float("inf")
cnt = [[0] * M for _ in range(N)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
recursion(0)
print(answer)