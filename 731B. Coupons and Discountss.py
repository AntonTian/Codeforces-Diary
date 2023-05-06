session = int(input())
teams = list(map(int,input().split()))
for i in range(session - 1):
    if teams[i] < 0:
        print('NO')
        break
    
    teams[i+1] -= teams[i] % 2

else:
    if teams[-1] % 2 == 0:
        print('YES')
    else:
        print('NO')
