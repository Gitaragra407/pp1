def fibonaci(n):
    if n==1 or n== 2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)

for i in range(1,51):
    print(fibonaci(i),end=" ")