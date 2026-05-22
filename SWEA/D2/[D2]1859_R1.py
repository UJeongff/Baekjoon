T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    sale = list(map(int, input().split()))

    max_price = 0
    profit = 0

    for day in range(N-1, -1, -1):

        today_price = sale[day]

        if today_price > max_price:
            max_price = today_price
        else: 
            profit += (max_price - today_price)

    print(f'#{test_case} {profit}')