mult=1
for a in range(1, 100):
  if a % 2==0:
    continue
  print(f'{mult}*{a}={mult*a}')
  mult=mult*a
  if mult >= 100:
    break