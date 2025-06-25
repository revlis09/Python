def greatest(data):
  greater=data[0]
  for i in range(1, len(data)):
    if greater<data[i]:
      greater=data[i]
  return greater

nums=[75, 80, 50, 85, 100, 95, 90, 65, 80, 70]
result=greatest(nums)
print(result)