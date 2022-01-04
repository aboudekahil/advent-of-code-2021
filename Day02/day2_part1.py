pos = [0,0]

def forward(x):
    pos[0]+=x

def down(x):
    pos[1]+=x

def up(x):
    pos[1]-=x

funcs = {
    "forward":forward,
    "down": down,
    "up": up
}

def call(func, par):
	funcs[func](int(par))

with open('./input.txt', 'r') as file:
    inputs = file.readlines()

for i in inputs:
    funct, par = i.split(" ")
    call(*i.split(" "))

print(pos[0] * pos[1])