a, b, c = map(int, input().split())

if a==b and b==c : 
    print(10000+a*1000)
elif a==b or b==c or c==a :
    if a==b:
        x=a
    elif b==c:
        x=b
    else :
        x=a
    print(1000+x*100)
else : 
    print(max(a,b,c)*100)
