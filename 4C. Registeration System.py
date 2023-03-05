names = int(input())
storage = {}
for i in range(names):
    insert = input()
    if insert not in storage:
        storage[insert] = 0
        print('OK')
    else:
        storage[insert] = str(int(storage[insert])+1)
        print(insert+storage[insert])
        storage[insert+storage[insert]] = 0
    