player, dragons = input().split()
player = int(player)
dragons = int(dragons)
atk0 = []
bonus0 = []
one = []
for i in range(dragons):
    atk, bonus = input().split()
    atk = int(atk)
    bonus = int(bonus)
    atk0.append(atk)
    bonus0.append(bonus)
    
one = zip(atk0, bonus0)
one = list(one)
true = sorted(one, key = lambda i: i[0])

atk0, bonus0 = zip(*true)

for i in range(dragons):
    if player > atk0[i]:
        player = player + bonus0[i]
    else:
        print("NO")
        exit()
print("YES")

    


