n = int(input())
arr = list(map(int, input().split()))
mostfreq = arr[0]
maxcount = 0
for num in arr:
    count = arr.count(num)
    if count > maxcount or (count == maxcount and num < mostfreq):
        maxcount = count
        mostfreq = num
print(mostfreq)
