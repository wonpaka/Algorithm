import sys
sys.stdin = open("BFS_graph.txt", "r")

# 최단거리 구하기 : 가중행렬을 주고 1 -> 3을 가는게 3칸이면 가중행렬에 3작성, 이 후 더 작은값이 있으면 작은값 작성

# 생각할점은 기준 수를 최대값으로 주고 줄여나간다 생각하기

from collections import deque

# 한점에서 다른점으로 가장 빨리가는 방법
# 1:N or N:1 이므로 visited는 1차원 리스트면 충분함
def BFS_s(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in range(1,N+1):
            # print(now, i, arr[now][i], visited_s[i],visited_s[now] + arr[now][i])

            # 1) 일단 길이 있고, 2) 해당 지점까지 가는 최단거리가 지금 거리보다 크면
            if arr[now][i] != 0 and visited_s[i] > visited_s[now] + arr[now][i]:

                visited_s[i] = visited_s[now] + arr[now][i]
                # 둘 사이의 거리 자체를 곧바로 가는길을 하나 만들어 버림!
                # 이렇게 되면 다음 연산이 매우 수월해짐
                
                # 현재 start -> now -> i 순서로 이동하는데 start -> i의 최단거리를 갱신해버림
                arr[start][i] = visited_s[i]

                q.append(i)


def BFS_b(end):
    q = deque()
    q.append(end)
    while q:
        now = q.popleft()
        for i in range(1,N+1):
            # 1) 일단 길이 있고, 2) 해당 지점까지 가는 최단거리가 지금 거리보다 크면
            if arr[i][now] != 0 and visited_b[i] > visited_b[now] + arr[i][now]:
                visited_b[i] = visited_b[now] + arr[i][now]
                arr[i][end] = visited_b[i]
                q.append(i)


T = int(input())
for test_case in range(1, T + 1):
    N, M, X = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for i in range(M):
        x, y, c = map(int, input().split())
        arr[x][y] = c

    visited_s = [float('inf')] * (N+1)
    visited_b = [float('inf')] * (N+1)
    visited_s[X] = 0
    visited_b[X] = 0
    BFS_s(X)
    # print(arr)
    BFS_b(X)

    answer = [visited_s[i+1] + visited_b[i+1] for i in range(N)]

    print('#{} {}'.format(test_case, max(answer)))
