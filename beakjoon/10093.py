a, b = input('').split(' ')

print(int(b)-int(a)-1)
for i in range(int(a)+1,int(b)) :
    print(i, end = ' ')