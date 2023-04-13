s = "abcdefghijklmnopqrstuvwxyz"*10
n = 1
i = 0

while i < len(s):
    for j in range(n):
        if i < len(s):
            print(s[i], end='')
            i +=1
        else:
            break
    print()
    n +=1