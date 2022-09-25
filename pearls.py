pearl = input()
print('NO' if len(pearl)%(pearl.count('o')or 1)else 'YES')