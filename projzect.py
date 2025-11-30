def funone(n):
    return n * (n+1) / 2
print(funone(4))
def funtwo(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(funtwo(4))
def fun3(n):
    sum = 0 
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum += 1
    return sum
print(fun3(4))