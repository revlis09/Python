scores=[['김정호',92,80,87],['박문수',94,82,86], ['이사부',74,65,69], ['장영실', 87,89,81]]
for row in scores:
  s_total=0
  for col in row[1:]:
    s_total=s_total+col
  avg=s_total/(len(row)-1)
  print(row[0],f'{avg:.2f}')