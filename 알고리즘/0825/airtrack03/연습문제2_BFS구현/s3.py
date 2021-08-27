"""
3. bfs - 인접 딕셔너리 구현
"""

def bfs(v):
    queue = [v]
    visited[v] = 1

    while queue:
        cur = queue.pop(0)
        print('방문 정점: {}, 방문 체크: {}'.format(cur, visited))
        for w in G[cur]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = dict()
for i in range(E):
    if G.get(temp[2*i]):
        G[temp[2*i]].append(temp[2*i+1])
    else:
        G[temp[2 * i]] = [temp[2*i+1]]

    if G.get(temp[2*i+1]):
        G[temp[2*i+1]].append(temp[2*i])
    else:
        G[temp[2*i+1]] = [temp[2*i]]
# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
# bfs 탐색 시작
bfs(1)