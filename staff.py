class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualify = q
    def __del__(self):
        print('До свидания, мистер ' + self.name + ' ' + self.surname)

a = Person(input('Имя:'),input('Фамилия:'), int(input('Квалификация:')))
b = Person(input('Имя:'),input('Фамилия:'), int(input('Квалификация:')))
c = Person(input('Имя:'),input('Фамилия:'))
print(a.name + ' ' + a.surname + ':' + str(a.qualify))
print(b.name + ' ' + b.surname + ':' + str(b.qualify))
print(c.name + ' ' + c.surname + ':' + str(c.qualify))
if a.qualify <= b.qualify and a.qualify <= c.qualify:
    del a
elif b.qualify <= a.qualify and b.qualify <= c.qualify:
    del b
else:
    del c   
input('Press any key to exit')    
