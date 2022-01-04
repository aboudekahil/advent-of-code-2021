with open('input.txt', 'r') as file:
    inputs = file.readlines()

prev = int(inputs[0])
count = 0
for i in inputs[1::]:
    if prev < int(i):
        count+=1
    prev = int(i)

print(count)