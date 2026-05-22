# 연월일 달력
# 날짜의 유효성을 판단하라.

# 출처: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

t = int(input())

for test_case in range(1, t+1):

    # str로 받아서 슬라이싱 가능하게
    date = input() 

    # 반복 표현을 변수로 추출
    year = date[0:4]
    month = int(date[4:6])

    # 8 인덱스가 없어도 범위 개념이라 오류를 안냄 
    day = int(date[6:8])

    if month <= 12 and month > 0:

        # in 연산자로 리스트 안에 값이 있는지 확인 / 없으면 not in
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31 and day >= 1:

                # 02d: 최소 두자리 정수, 빈자리는 0으로 채우기
                print(f"#{test_case} {year}/{month:02d}/{day:02d}")
            else:
                print(f"#{test_case} -1")
        elif month in [4, 6, 9, 11]:
            if day <= 30 and day >= 1:
                print(f"#{test_case} {year}/{month:02d}/{day:02d}")
            else: 
                print(f"#{test_case} -1")
        elif month == 2:
            if day <= 28 and day >= 1:
                print(f"#{test_case} {year}/{month:02d}/{day:02d}")
            else: 
                print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")