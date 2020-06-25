def stan (a):
    if a=="":
        return 0,""
    else:
        l,s=stan(a[:-1])
        return l+1, a[-1]+s

print(stan(input()))
