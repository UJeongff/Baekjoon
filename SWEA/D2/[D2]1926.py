# 간단한 369게임
# 3, 6, 9 있는 개수만큼 박수(-) 출력

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq

N = int(input()) # 범위

for i in range(1, N+1):
    count = 0 # 박수 횟수 카운터, i마다 리셋

    for c in str(i): # 한 글자씩 순회하기 위해 문자열로 변경 
        if c in ['3', '6', '9']: # i가 문자열이기 때문에, '369'로 대체 가능
            count += 1
        
    if count == 0:
        print(i, end=' ')
    else:
        print('-'*count, end=' ')