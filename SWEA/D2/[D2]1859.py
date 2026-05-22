# 백만 장자 프로젝트
# 사재기를 하여 최대한 이득을 얻도록 도와주자. 
# line1: test_case 개수
# line2: 주식 가격을 알고 있는 N일
# line3: 가격
# ..
# ex1: 가격이 10 7 6 -> 살수록 손해니까 안 삼 = 0
# ex2: 가격이 3 5 9 -> 1일(3)에 사서 3일(9)에 팔면 +6, 2일(5)에 사서 3일(9)에 팔면 +4로 총 이익 10
# 뒤에서부터 훑으며 (최댓값 - 오늘 가격)을 계속 더하는 아이디어 
# Greedy 알고리즘: 매 순간 가장 이득인 선택을 하는 것 

# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    max_price = 0

    for i in range(N-1, -1, -1): # (시작, 끝, 간격): 마지막 인덱스에서 시작
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]
    
    print(f"#{tc} {profit}")
