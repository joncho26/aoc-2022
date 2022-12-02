f = open('./file.txt','r')

data = f.read().split('\n')



# part 1
max = 0
total = 0
sums = []
for num in data:
  if num == '':
    sums.append(total)
    total = 0
  else: 
    total = total + int(num)
  
for num in sums:
  if num > max:
    max = num



# part 2
sorted_sums = sorted(sums)
sum_of_largest_3 = sum(sorted_sums[-3:])