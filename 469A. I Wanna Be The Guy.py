levels = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
start = 1
x.pop(0)
y.pop(0)

for i in range(levels):
    if int(start) in x or int(start) in y:
        start += 1
        
    else:
        print("Oh, my keyboard!")
        exit()
        
print("I become the guy.")
    
        
    
