n = int(input())
numbers = list(map(int, input().split()))
maxelement = numbers[0]
maxposition = 1  
for i in range(1, n):
    if numbers[i] > maxelement:
        maxelement = numbers[i]
        maxposition = i + 1  
print(maxposition)
