#march long challenge
n,h,x = list(map(int,input().split()))
n_v = list(map(int,input().split()))

for i in range(len(n_v)):
    if any(n_v[i] + x >= h for i in range(len(n_v))):
        print("YES")
        break
    elif n_v[i] + x < h:
        print("NO")
        break
