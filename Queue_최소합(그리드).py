import sys

sys.stdin = open('Queue_최소합(그리드).txt', 'r')


# 방사형으로 모든 경우의수를 탐색하고 낮은값만 찾아 거꾸로 올라옴

def DFS(x, y):
    down = right = N * 11  # 범위 밖 가상의 값 (max 로 설정)
    if x == y >= N - 1:  # 마지막 지점 도착
        # print('[last]', arr[x][y], x, y, depth)
        return arr[x][y]

    # 아래끝 or 오른끝일 경우
    else:
        if x < N - 1:
            down = DFS(x + 1, y)
        if y < N - 1:
            right = DFS(x, y + 1)

    # 현재값에 더 작은값을 더함
    # 여기서 down과 right의 경우 재귀적으로 계속 돌아감
    # 완전탐색이나 탐색값중 합이 작은값만 출력하게 됨
    # 결국 main 함수에선 최소합이 출력된다.

    # 출력을 뽑으면 역순으로 재귀가 들어옴
    # print(down, right)
    if down < right:
        # print('down < right', down + arr[row][col], row, col, depth)
        return arr[x][y] + down
    else:
        # print('down > right', right + arr[row][col], row, col, depth)
        return arr[x][y] + right


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {DFS(0, 0)}')

