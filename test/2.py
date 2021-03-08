#카지노 https://www.acmicpc.net/problem/2798


a, b = list(map(int, input().split()))
data = list(map(int, input().split()))

result = 0
lenth = len(data)

for i in range(0, lenth) :
    for j in range(i+1, lenth):
        for k in range(j+1, lenth) :
            sum_value = data[i] +data[j] + data[k]
            if sum_value <= b:
                    result = max(result, sum_value)

print(result)
