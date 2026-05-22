# 홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라. 

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&

t = int(input())

for test_case in range(1, t+1):
    numbers = map(int, input().split())
    total = 0

    for num in numbers:
        if num%2 == 1:
            total += num

    print(f"#{test_case} {total}")