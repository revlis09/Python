medal = [[6, 4, 10], [38, 32, 19], [26, 14, 17]]
medal_1 = ['금', '은', '동']

totals = [0, 0, 0]

for row in medal:
    for i in range(3):
        totals[i] += row[i]

for i in range(3):
    print(medal_1[i], totals[i])