[a, b, c] = input().split()
[A, B, C] = int(a), int(b), int(c)
print("{}\n{}\n{}\n{}".format( ((A+B)%C), (((A%C)+(B%C))%C), ((A*B)%C), (((A%C)*(B%C))%C)  ))