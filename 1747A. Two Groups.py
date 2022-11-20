tians = int(input())
for number in range(tians):
    numbers = int(input())
    collect = [int(x) for x in input().split()]
    s1 = 0
    s2 = 0
    for i in collect:
        if i >= 0:
            s1 += i
        else:
            s2 -= i
    print(abs(s1 -s2))