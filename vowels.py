def vowels(a=""):
    if a=="":
        return 0
    else:
        if 'aeiou'.find(a[0])==-1:
            n=0
        else:
            n=1
        return n +  vowels(a[1:])

print(vowels(input('Give me a string:')))
for i in range (10):
    print(i)
