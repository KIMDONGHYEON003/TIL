'''
3. bfs - 인접 딕셔너리 구현
'''

import queue


def bfs(v):
    q = queue.Queue()
    q.put(v)

    while not q.empty():
        node = q.get()
        if not visited[node]:
            visited[node] = True
            for e in linked.get(node):
                q.put(e)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
v, e = map(int, input().split())

# 간선 정보 초기화
linked = {}

# Graph 초기화
in_list = list(map(int, input().split()))
for i in range(len(in_list)//2):
    linked[in_list[i*2]] = linked.get(in_list[i*2], []) + [in_list[i*2+1]]
    linked[in_list[i*2+1]] = linked.get(in_list[i*2+1], []) + [in_list[i*2]]

# 방문 표시 초기화
visited = [False] * (v+1)

# bfs 탐색 시작
bfs(1)