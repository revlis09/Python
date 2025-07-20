n = int(input())  
daylist = []
for i in range(n): 
    att = input().split()
    daylist.append(att)
count = 0  

for student in daylist:
    for day in student:
        if day == '1':
            count += 1

print(count)