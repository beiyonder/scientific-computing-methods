n, m= map(int, input().split())

coeff_n = list(map(int, input().split()))

coeff_m = list(map(int, input().split()))

def prod(coeff_n, coeff_m):
    

    res = [0]*(m+n+1)

    for i in range(n +1):
        for j in range(m+1):
            res[i+j] += coeff_n[i]*coeff_m[j]
    return res

print(prod(coeff_n, coeff_m))