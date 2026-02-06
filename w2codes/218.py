n = int(input())
strings = [input().strip() for _ in range(n)]
unique = []
indices = []
for i in range(n):
    s = strings[i]
    if s not in unique:
        unique.append(s)
        indices.append(i + 1)  
for s in sorted(unique):
    print(s, indices[unique.index(s)])
