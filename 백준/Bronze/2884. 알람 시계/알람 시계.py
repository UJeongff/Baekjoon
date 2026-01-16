h, m = map(int, input().split())

if m < 45 and h != 0 :
    H = h-1
    M = m+15
elif m < 45 and h == 0 :
    H = 23
    M = m+15
else :
    H = h
    M = m-45
print(H, M)