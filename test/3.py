## 스택 : https://www.acmicpc.net/problem/1874##
a = int(input())

count = 1
stack =[]
result = []

for i in range(1,a+1) :
    data = int(input())
    while count <= data :
        stack.append(count)
        count +=1
        result.append('+')
    if stack[-1] == data :
        stack.pop()
        result.append('-')
    else :
        print('NO')
        exit()

print('\n'.join(result))

