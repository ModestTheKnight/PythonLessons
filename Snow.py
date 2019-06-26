class Snow:
    def __init__(self, n):
        self.value = int(n)
    def __add__(self, o):
        self.value += o
    def __sub__(self, o):
        if o > self.value:
            self.value = 0
        else:
            self.value -= o 
    def __mul__(self, o):
        self.value *= o
    def __truediv__(self, o):
        self.value = round(self.value / o)
    def __call__(self, n):
        self.value = int(n)
    def makeSnow(self, f):
        r = self.value//f
        l = self.value%f
        return '\n'.join(['*' * f for i in range(r)]) + '\n' + '*' * l
    def __repr__(self):
        return '*' * self.value

s = Snow(input('SnowFlakes: '))
print(s)
s(input('SnowFlakes: '))
print(s)
s + int(input('add SnowFlakes: '))
print(s)
s - int(input('sub SnowFlakes: '))
print(s)
s * int(input('mul SnowFlakes: '))
print(s)
s / int(input('div SnowFlakes: '))
print(s)
print(s.makeSnow(int(input('lets snow: '))))
