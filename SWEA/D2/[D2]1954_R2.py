# 달팽이 숫자

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 달팽이는 행으로 채우는 게 아니라 한 칸씩 채우는 로직
    # 빈 NxN 2차원 배열 초기화 
    arr = [[0] * N for _ in range(N)]

    # 현재 위치, 방향
    r, c = 0, 0
    d = 0 

    # 1부터 N^2까지 반복 
    for row in range(1, N*N+1):
        # 현재 칸에 숫자 넣기 
        arr[r][c] = row

        # 방향 변경 전 계산된 좌표
        nr = r + dr[d]
        nc = c + dc[d]

        # 벽 밖으로 나갔거나, 이미 채워졌으면 방향 변경  
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
            d = (d+1) % 4

            # 방향 변경 후 새 방향으로 다시 계산된 좌표 
            nr = r + dr[d]
            nc = c + dc[d]

        # 한 칸 이동(실제 이동)
        r, c = nr, nc 


    print(f'#{test_case}')
    for line in arr:
        # *: 리스트를 풀어서 공백으로 구분해서 출력 
        print(*line)
