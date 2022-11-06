tians = input()
tians = int(tians)
for number in range(tians):
    size, rooks = (input().split())
    size = int(size)
    rooks = int(rooks)
    for i in range(rooks):
        x, y = (input().split())
        x = int(x)
        y = int(y)
    if rooks >= size:
        print('NO')
    else:
        print('YES')
        
    