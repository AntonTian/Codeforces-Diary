tians, limit = input().split()
tians = int(tians)
limit = int(limit)
hrs = []
mins = []

for number in range(tians):
    h , m = (input().split())
    h = int(h)
    m = int(m)
    hrs.append(h)
    mins.append(m)
    
hnext = 0
mnext = 0

for x in range(len(hrs)):
    timecomp = (hrs[x] - hnext)*60 + mins[x] - mnext
    if timecomp >= limit + 1:
        break
    mnext = mins[x] + limit + 1
    hnext = hrs[x]
    
    if mnext >= 60:
        hafter = mnext // 60
        hnext += hafter
        mnext -= hafter*60
        
print(hnext, mnext)
    

 

        