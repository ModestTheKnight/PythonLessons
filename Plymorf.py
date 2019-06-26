class A:
    def __init__(self, v):
        self.value = set(str(v))
    def __add__(self, o):
        return self.value.union(set(str(o)))
    def __radd__(self, o):
        return self.value.intersection(set(str(o)))
    def __str__(self):
        return ' '.join([str(i) for i in self.value])                               

a = A(input())
b = input()
print(a)
print(a + b)
print(b + a)                                       
                                       
