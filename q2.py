t = int(input())
             
while(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    even, odd = 0, 0
    for i in range(n):
        if a[i]%2:
            odd += 1
        else:
            even += 1
    if even == 1 and odd == 1:
        print(2)
        
    else:
        print(max(even, odd))
    
    t -= 1


