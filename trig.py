import series
def sin (x, precision=0.001,n=0):
    s = (-1)**n*x**(2*n+1)/series.factor(2*n+1)
    if abs(s)<=precision:
        return s
    else:
        return s + sin(x, precision, n+1)
def cos (x, precision=0.001,n=0):
     s = (-1)**n*x**(2*n)/series.factor(2*n)
     if abs(s)<=precision:
         return s
     else:
         return s + cos(x, precision, n+1)
