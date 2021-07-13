c = int(input(''))
n = []
for i in range(c):
    a, b = map(int,input('').split())
    n.append(a+b)

for i in range(c):
    print(f'Case #{i+1}: {n[i]}')