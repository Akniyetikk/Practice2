n = int(input())
array = list(map(int, input().split()))
minelement = min(array)
maxelement = max(array)
for i in range(n):
    if array[i] == maxelement:
        array[i] = minelement
print(*array)
