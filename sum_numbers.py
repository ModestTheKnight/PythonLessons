def sum_numbers (n):
    return 1 if n==1 else n + sum_numbers(n-1)


print(sum_numbers(int(input('>>'))))
