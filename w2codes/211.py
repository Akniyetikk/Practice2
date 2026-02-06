n, l, r = map(int, input().split()) 
array = list(map(int, input().split()))
lindex = l - 1
rindex = r - 1
array[lindex:rindex+1] = array[lindex:rindex+1][::-1]
print(*array)
