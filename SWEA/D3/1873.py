# 상호의 배틀필드

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc

T = int(input())

# 기호, 문자열에 대한 동작 정의 (딕셔너리)
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
direction = {'U': '^', 'D': 'v', 'L': '<', 'R': '>'}
shoot = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    arr = []

    # weight에 대한 반복문 필요 없음
    for height in range(H):
        row = list(input())
        arr.append(row)

    N = int(input())
    active = list(input())

    # 맵에서 탱크 위치, 방향 찾기 
    for height in range(H):
        for weight in range(W):

            # in: arr[i][j]가 '^v<>' 안에 있는지 확인
            if arr[height][weight] in '^v<>':
                x, y = height, weight
                d = arr[height][weight]

    # 명령 한 글짜씩 처리 (이동) 
    for cmd in active: 
        if cmd != 'S':     # move 딕셔너리에 'S' 없음 
            d = direction[cmd]    # 방향 변경
            arr[x][y] = d         # 이동 없어도 방향은 변경됨
            dx, dy = move[cmd]    # 이동량 꺼내기 
            nx = x + dx
            ny = y + dy 
            
            # H, W 을 벗어나지 않고 평지인지 확인 
            if 0<=nx<H and 0<=ny<W and arr[nx][ny]=='.': 
                arr[x][y] = '.'    # 떠난 자리 평지
                arr[nx][ny] = d    # 새 자리에 탱크
                x, y = nx, ny      # 좌표 캥신

        # 포 쏘기(S)
        else: 
            # 포탄 위치(탱크 방향(d))
            dx, dy = shoot[d]
            px, py = x, y 

            while True: 
                px += dx
                py += dy 
                if px>=H or py>=W or px<0 or py<0: 
                    break
                if arr[px][py]=='#':
                    break
                if arr[px][py]=='*':
                    arr[px][py] = '.'    # 평지
                    break 

    # 결과 출력 
    for i in range(H):
        if i == 0:
            # arr는 글자 리스트, 그냥 출력하면 대괄호와 따옴표가 다 출력됨
            print(f'#{test_case} ' + ''.join(arr[i]))
        else: 
            print(''.join(arr[i]))
