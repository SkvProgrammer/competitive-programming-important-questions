t = int(input())

while t:
    n = int(input())
    word_s = set(map(str,input().lower().split()))
    words = list(word_s)
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i][0] == words[j][0]:
                continue
    print("0")
        
    t-=1
