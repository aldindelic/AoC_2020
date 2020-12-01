f = open('ad1.txt', 'r').readlines()
ans1 = 0
ans2 = 0
for i in f:
    for j in f:
        if int(i) + int(j) == 2020:
            ans1 = int(i) * int(j)
        for k in f:
            if int(i) + int(j) + int(k) == 2020:
                ans2 = int(i) * int(j) * int(k)
print('ANS1:-->   ', ans1)
print('ANS2:-->   ', ans2)
