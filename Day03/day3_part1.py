with open('./input.txt', 'r') as file:
    inputs = file.readlines()

l = list(zip(*inputs))

gamma = ""
epsilon = ""

for i in l:
    gamma += str((i.count('1') > i.count('0')) + 0)
    epsilon += str((i.count('1') < i.count('0')) + 0)


print(int(gamma, 2) * int(epsilon, 2))
