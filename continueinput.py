mylist = []
v = True
while v:
    n = int(input())
    mylist.append(n)
    wish = input("Do you want to continue or exit(enter c for continue and e for exit)?")
    if wish == "c" or wish == "C":
        v = True
    elif wish == "e" or wish == "Q":
        v = False

mylist.sort()
print("Numbers in ascending order:",end="")
for i in mylist:
    print(i,end = " ")

     