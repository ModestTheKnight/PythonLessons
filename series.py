def factor (x):
    if x==0:
        return 1
    elif x==1:
        return 1
    else:
        return x*factor(x-1)
def fibo (f=1):
    if f==1:
        return 0,1
    else:
        a,b = fibo (f-1)
        return b,a+b
