scores=[[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81]]
for row in scores:
  s_total=0
  for col in row:
    s_total=s_total+col
  avg=s_total/len(row)
  print(f"{avg:.2f}")