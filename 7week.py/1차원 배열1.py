planetScale=[2240, 6052, 6378, 3390, 69911, 58232, 25362, 24622]
maxScale=planetScale[0]
for i in range(1, 8):
  if maxScale<planetScale[i]:
    maxScale=planetScale[i]
print(maxScale)