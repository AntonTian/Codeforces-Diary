name = int(input())
store = input()
counter = 0
fixed = 0

for i in range(name):
    if store[i] == "x":
        counter += 1
    else:
        if counter >= 3:
            fixed += counter - 2
        counter = 0

if counter >= 3:
    fixed += counter - 2          
            
print(fixed)
            