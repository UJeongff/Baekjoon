# 파리 퇴치 

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

T = int(input())

for test_case in range(1, T+1):
    max_flies = 0 

    # int는 값 하나만 바꿈 -> map 사용 
    N, M = map(int, input().split())

    # 격자는 N줄에 걸쳐 들어와서 N번 받아야 함 
    # 받은 줄들을 arr에 쌓아야 함 
    arr = []
    for flies in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # N*N 격자에서 파리채는 M*M
    # 가능한 파리채 범위는 인덱스로 0 ~ N-M 
    # i: 모서리의 행 번호, j: 모서리의 열 번호
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0 
            
            # (i, j)에 파리채를 둠
            # 파리채가 덮는 MxM칸을 다 더해야 total이 나옴 
            for di in range(M):
                for dj in range(M):
                    total += arr[i+di][j+dj]
            
            if total > max_flies:
                max_flies = total
            
    print(f'#{test_case} {max_flies}')