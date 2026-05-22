# 색칠하기 

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTLZMRKpsYDFAVT

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    purple = 0 

    # 10x10 격자 초기화 
    arr = [[0]*10 for _ in range(10)]

    for box in range(1, N+1):
        r1, c1, r2, c2, color = map(int, input().split())
        
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += 1
            
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                purple += 1
    
    print(f'#{test_case} {purple}')