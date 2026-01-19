a, b = map(int, input().split())
c = int(input())
x = b+c

if x < 60: 
    print(a, x)
else : 
    print((a+(x//60))%24, x%60)