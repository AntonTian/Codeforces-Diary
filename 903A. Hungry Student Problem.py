chicken = input()
chicken = int(chicken)
for x in range(chicken):
    x = int(input())
    if x % 3 == 0 or x % 7 == 0 or x % 10 == 0 or x > 12:
        print("YES")
    else:
        print("NO") 