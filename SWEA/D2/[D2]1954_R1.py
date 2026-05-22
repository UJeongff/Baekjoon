# 달팽이 숫자

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    d = 0

    arr = [[0]*N for _ in range(N)]

    for row in range(1, N*N+1):
        arr[r][c] = row
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
            d = (d+1) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        r, c = nr, nc
    
    print(f'#{test_case}')
    for line in arr:
        print(*line)

