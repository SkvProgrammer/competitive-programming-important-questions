#highest divisor

a = int(input())

div_a = []

for i in range(1,500):
    if i%a == 0:
        div_a.append(i)

print(div_a)
for i in range(1,11):
    if i in div_a:
        print(i)
        
