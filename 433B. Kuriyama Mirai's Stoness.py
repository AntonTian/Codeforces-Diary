stones = int(input())
cost = list(map(int,input().split()))
steps = sorted(cost)
q1s = [0]
q2s = [0]
q1 = 0
q2 = 0
for i in range(stones):
    q1 += cost[i]
    q2 += steps[i]
    q1s.append(q1)
    q2s.append(q2)
    
qna = int(input())
for i in range(qna):
    tian, first, second = map(int,input().split())
    if tian == 1:
        one = print(q1s[second] - q1s[first-1])
    elif tian == 2:
        two = print(q2s[second] - q2s[first-1])