f = open('travels.txt', 'r')
travels1 = 0
travels2 = 0
travels3 = 0
colvo_m = 0
colvo_m1 = 0
colvo_m2 = 0
colvo_m3 = 0
way = 0
otprav_punkt = {}
colvo1 = 0
prin_punkt = {}
colvo2 = 0
prin_punkt2 = {}
for i in f:
    a = i.split()
    if a[2] == 'Липки':
        colvo_m += int(a[6])
    if int(a[0]) == 1:
        travels1 += 1
        colvo_m1 += int(a[6])
        way += int(a[4])
    if int(a[0]) == 2:
        travels2 += 1
        colvo_m2 += int(a[6])
    if int(a[0]) == 3:
        travels3 += 1
        colvo_m3 += int(a[6])

    otprav_punkt[a[2]] = 0

    for j in otprav_punkt:
        if a[2] == j:
            otprav_punkt[j] += int(a[6])

    prin_punkt[a[3]] = 0
    prin_punkt2[a[3]] = 0

    for j in otprav_punkt:
        if a[3] == j:
            prin_punkt[j] += int(a[6])
            prin_punkt2[j] += int(a[5]) / int(a[4])


if travels1 > travels2 and travels1 > travels3:
    print('1 октября', colvo_m1)
elif travels2 > travels1 and travels2 > travels3:
    print('2 октября', colvo_m2)
else:
    print('3 октября', colvo_m3)

print(colvo_m)
print(way)
print(otprav_punkt)
print(len(otprav_punkt))
print(prin_punkt)
print(len(prin_punkt))
print(max(prin_punkt2, key=prin_punkt2.get))
f.close()