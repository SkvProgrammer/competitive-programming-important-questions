#my solution(TLE error)
"""
t = int(input())
d = 0
l_a = []
l_b = []
p_l_a_b = []
while t:
    c = int(input())
    for i in range(1,c):
        if 2**i > c:
            d = i
            break
    for a in range(1,2**d):
        for b in range(1,2**d):
            if a^b == c:
                l_a.append(a)
                l_b.append(b)

    for i in range(len(l_a)):
        if l_a[i] ^ l_b[i] == c:
            p_l_a_b.append(l_a[i] * l_b[i])
            
    print(max(p_l_a_b))
    l_a.clear()
    l_b.clear()
                
    t-=1
    
"""

#correct solution
from math import log

for _ in range(int(input())):
    c = int(input())
    b = 2**int(log(c, 2)) - 1
    a = c ^ b
    print(a*b)
