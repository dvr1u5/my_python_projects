frst, scnd, thrd, frth = input().split()
frst = int(frst)
scnd = int(scnd)
thrd = int(thrd)
frth = int(frth)
bus1 = set()
bus2 = set()
for i in range(min(frst, scnd), max(frst, scnd) + 1):
    bus1.add(i)
for i in range(min(thrd, frth), max(thrd, frth) + 1):
    bus2.add(i)
print(len(bus1 & bus2))
