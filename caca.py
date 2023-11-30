clous = 15
size = 5

case = {}

for i in range(size):
    for y in range(size):
        case[i,y] = 0

objectif = {}

for i in range(size):
    for y in range(size):
        case['o',i,y] = 0

print(case)

for i in range(clous):
#    nom = f'Fonction {i+1}'
    def f(i):
        print(i)
    f(i)
f(3)

