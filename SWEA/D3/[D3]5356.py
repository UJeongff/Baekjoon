# 의석이의 세로로 말해요

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO

T = int(input())

for test_case in range(1, T+1):
    arr = []
    for n in range(5):
        
        # 문자열이고, 사이에 공백 없음 
        text = list(input())
        arr.append(text)
    
    # 빈문자열 
    total = ""
    for j in range(15): # 열(글자 자리, 5행 다 읽을 때까지 고정)
        for i in range(5): # 행(5줄)

            # "j번 글자가 i번 줄에 존재하는지
            if j < len(arr[i]): # j < i번 줄의 글자 개수 
                # .index(x): x의 값이 어느 위치에 있는지 출력
                # list[x]: x번째 인덱스 값 출력 
                total += arr[i][j] # arr[줄][글자]
    
    print(f'#{test_case} {total}')