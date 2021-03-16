t = int(input())

for i in range(t):
    r = input().split('0')
    print(r)
    newr = [x for x in r if x!= '']
    print(len(newr))
    
