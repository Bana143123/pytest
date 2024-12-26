def fact(n):
    if n<0:
        raise ValueError("Factorial is not supported for negative numbers.")
    if n<=1:
        return 1
    
    return n*fact(n-1)

