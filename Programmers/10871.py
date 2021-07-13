a,b = map(int,input('').split())
n = list(map(int,input().split()))
# a = 10
# b = 5
# n = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
answer = ''
for i in n:
    if i < b:
        answer += str(i) + ' '

print(answer[:-1])