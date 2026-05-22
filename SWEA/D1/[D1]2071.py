# 평균값 구하기
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라. 

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T+1):
    numbers = map(int, input().split())
    total = 0
    avg = 0

    for num in numbers:
        total += num 

    avg = total / 10 + 0.5
    print(f"#{test_case} {int(avg)}")