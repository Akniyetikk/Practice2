n = int(input())
arr = list(map(int, input().split()))
check = []  
for num in arr:
    if num not in check:
        print("YES")
        check.append(num) 
    else:
        print("NO")
