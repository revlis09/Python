medal = [['대한민국',6, 4, 10], ['중국',38, 32, 19], ['일본',26, 14, 17]]
for i in medal:
  total=0
  for j in i[1:]:
    total+=j
  print(i[0], total)
  