with open('input.txt', 'r') as file:
    inputs = list(map(int,file.readlines()))

l = []
for indx, _ in enumerate(inputs):
    if indx < len(inputs)-2:
        l.append([inputs[indx], inputs[indx+1], inputs[indx+2]])

inputs = list(map(sum,l))


prev = inputs[0]
count = 0

for i in inputs:
    if i > prev:
        count+=1
    prev = i

print(count)