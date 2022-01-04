from typing import Counter


with open('.\input.txt', 'r') as file:
    inputs = file.readlines()

inputsv2 = inputs.copy()
l = list(zip(*inputs))
l2 = list(zip(*inputsv2))
indx = 0
while (len(inputs) > 1):
    mc = str((l[indx].count('1') >= l[indx].count('0')) + 0)
    inputs = list(filter(lambda x: True if x[indx] == mc else False, inputs))
    l = list(zip(*inputs))
    indx += 1

indx = 0

while (len(inputsv2) > 1):
    lc = '0' if l2[indx].count('0') <= l2[indx].count('1') else '1'
    # print(lc)
    inputsv2 = list(
        filter(lambda x: True if x[indx] == lc else False, inputsv2))
    l2 = list(zip(*inputsv2))

    indx += 1

print(int(inputs[0], 2) * int(inputsv2[0], 2))