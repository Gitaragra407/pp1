def pow(a,n):
    if n == 0:
        return 1
    else:
        if n==1:
            return a
        else: 
            return a*pow(a,n-1)

print(pow(5, 3))