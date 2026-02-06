n = int(input())                
array = list(map(int, input().split()))  
newarray = [x**2 for x in array]
print(*newarray)

