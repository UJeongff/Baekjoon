# 파리퇴치3 

# 출처: https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa

T = int(input())

t = [(-1,0), (1,0), (0,-1), (0,1)]
x = [(-1,-1), (-1,1), (1,-1), (1,1)]

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = []

    # 파리 배열
    for i in range(N):
        fly = list(map(int, input().split()))
        arr.append(fly)
    
    # 스프레이 (중심 고정 아님)
    ans = 0 # 최댓값 담을 변수
    for i in range(N):
        for j in range(N):

            total = arr[i][j]
            for dx, dy in t:
                for k in range(1, M):
                    nx = i + dx*k 
                    ny = j + dy*k 
                    if 0<=nx<N and 0<=ny<N:
                        total += arr[nx][ny]
            
            total_x = arr[i][j]
            for dx, dy in x:
                for k in range(1, M):
                    nx = i + dx*k 
                    ny = j + dy*k 
                    if 0<=nx<N and 0<=ny<N:
                        total_x += arr[nx][ny]
            
            ans = max(ans, total, total_x)
        
    print(f'#{test_case} {ans}')