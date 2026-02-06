n = int(input())
if n < 1:
    print("NO")
else:
    power_ = 1
    while power_ < n:
        power_ *= 2
    if power_ == n:
        print("YES")
    else:
        print("NO")
