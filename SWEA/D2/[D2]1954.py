# 달팽이 숫자
# 2차원 배열에 1부터 N*N까지 시계방향으로 채우기

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    #  오른, 아래, 왼, 위
    dr = [0, 1, 0, -1] # 행 변화
    dc = [1, 0, -1, 0] # 열 변화

    # 반복 횟수만 필요해서 변수를 안쓰고 _를 사용
    arr = [[0]*N for _ in range(N)] # NxN 빈 배열
    r = 0 # 현재 행 위치
    c = 0 # 현재 열 위치
    d = 0 # 현재 방향 (0=오른쪽, 1=아래, 2=왼쪽, 3=위)

    for num in range(1, N*N+1):

        # ex) num = 3일 때, arr[0][2] = 3 / nr = 0 + 0 = 0 / nc = 2 + 1 = 3 
        arr[r][c] = num
        nr = r + dr[d]
        nc = c + dc[d]

        # nr < 0: 위로 벗어남
        # nr >= N: 아래로 벗어남
        # nc < 0: 왼쪽으로 벗어남
        # nc >= N: 오른쪽으로 벗어남
        # arr[nr][nc] != 0: 이미 채워진 칸 
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:

            # %4 = 방향 개수
            # 0=오른쪽, 1=아래, 2=왼쪽, 3=위 

            # ex) nc >= N -> 3>=3 이므로 방향 전환 필요
            # d: 0->1 아래로 방향전환, nr=0+1=1 아래로, nc=2+0=2 열은 그대로 
            d = (d+1) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        r, c = nr, nc

    print(f"#{test_case}")
    for row in arr:
        print(*row) # *row로 리스트를 풀어서 출력
