#author:Satyam kumar verman(SkvProgrammmer)
#march long challenge
#competitive programming

#number of test cases
t = int(input())
d = []
s = 0
diff = 0
#starting the while loop
while t:
    n = int(input())
    #multiple inputs
    n_i = list(map(int,input().split()))
    #sorting the list
    n_i.sort()  
    for i in range(n):
        if n_i[i] > i + 1:
            print("Second")
        elif n_i[i] < i + 1:
            s+=((i+1)-n_i[i])
            if s%2 == 0:
                print("First")
                break
            if s%2 != 0:
                print("Second")
                break

        
        t-=1



