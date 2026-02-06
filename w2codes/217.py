n = int(input())
numbers = [input().strip() for _ in range(n)]
result = 0
for num in numbers:
    if numbers.count(num) == 3:
        result += 1
print(result // 3)
