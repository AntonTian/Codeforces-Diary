lock = int(input())
combs = 0
counter = lock-1
for i in range(1, lock, 1):
    combs += (i*counter)  
    counter -= 1

combs += lock
print(combs)
