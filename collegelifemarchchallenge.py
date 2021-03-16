#college life 4

t = int(input())


while t:
    n,e,h,a,b,c = list(map(int,input().split()))
    if e == h and e < n:
        print("-1")
    elif e > n and h > n and c == max([a,b,c]):
        print(n * min([a,b,c]))
    elif e > n and h > n and a == max([a,b,c]) and c == min([a,b,c]):
        print(int(min([a,b,c]) * n/2 + max([a,b,c]) * n/n + b * 1))
    t-=1
