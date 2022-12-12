def sum(N):
    if N<1:
        return "number must be greater or equal to 1"
    else:
        if N==1:
            return 1
        else:
            return N+sum(N-1)

print(sum(10))