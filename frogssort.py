#frogssortproblemlongchallengecodechef

t = int(input())

while t:
    n = int(input())
    w = list(map(int,input().split()))
    l = list(map(int,input().split()))
    i = 0
    s = 1
    s1 = 1
    for i in range(0, len(w)):
        for j in range(i+1, len(w)):
            if(w[i] > w[j]):
                s = s + 1
                temp = w[i]
                w[i] = w[j]    
                w[j] = temp

                if(l[i] > l[j]):
                    s1 = s1 + 1 
                    temp = l[i]
                    l[i] = l[j]    
                    l[j]= temp
                


    print(s + s1)
    
    t-=1
