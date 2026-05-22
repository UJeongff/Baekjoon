# B−A가 짝수라면, A의 값에 2를 곱하기
# 그렇지 않으면, B의 값에 17 더하기 
# A >= B 만족할 때까지 반복하고, 만족하면 그 횟수 출력

A=int(input())
B=int(input())

count = 0

while A < B:
    x = B-A

    if x%2 == 0:
        A = A*2
    else: 
        B = B+17 

    count += 1

print(count)