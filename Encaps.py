from random import random, shuffle, randint

class Hidden:
    __objects=[]
    def __init__(self):
        self.__field1, self.__field2, self.__field3, self.__field4 = Hidden.__makeObjectAttr()
        #self.field1, self.field2, self.field3, self.field4 = Hidden.__makeObjectAttr()
        Hidden.__objects.append(self)
    def __del__(self):
        Hidden.__objects.remove(self)
    def getObjectCount():
        return len(Hidden.__objects)
    def getObjectList():
        return Hidden.__objects
    def __makeObjectAttr():
        rl = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        shuffle(rl)
        start = round(random()*len(rl))
        stop = round(random()*len(rl))
        if start>stop:
            step = -1
        else:
            step = 1
        f1 = round(random()*100)
        f2 = ''.join([l for l in rl])[start:stop:step]
        f3 = bool(round(random()))
        f4 = [2**x for x in range(randint(1,10))]
        return f1, f2, f3, f4
    #def __setattr__(self, attr, value):
    #    print(attr)
    #    if attr in {'__field1', '__field2', '__field3', '__field4'}:
    #        self.__dict__[attr] = value
    #    else:
    #        raise AttributeError
    def setItem(self, attr, value):
        h_attr = '_Hidden__' + attr
        if h_attr in self.__dict__:
            self.__dict__[h_attr] = value
        else:
            raise AttributeError
    def getItem(self, attr):
        h_attr = '_Hidden__' + attr
        if h_attr in self.__dict__:
            return self.__dict__[h_attr]
        else:
            raise AttributeError
    def __str__(self):
        attrlist = []
        for f, v in self.__dict__.items():
            attrlist.append(': '.join([f[9:], str(v)]))
        return '\n'.join(attrlist)  

a = int(input('Enter objects amount: '))
for _ in range(a):
    Hidden()
print('Objects created: ' +str(Hidden.getObjectCount()))
print('Operation with objects \n=======================')
count = 0
for o in Hidden.getObjectList():
    count += 1
    print('Object' + str(count) + '\n==============')
    print(o)
    print('get attribute')
    try:
        print('o.field1')
        print(o.field1)
    except:
        print('Use getItem() method')
    try:
        print('o.getItem()')
        print(o.getItem('field1'))
    except:
        print('No attribute')
    print('set attribute')
    try:
        o.field2 = 'Hello, I am Object' + str(count)
    except:
        print('Use setItem() method')
    try:
        print('o.setItem()')
        print('<==' + o.getItem('field2'))
        o.setItem('field2', 'Hello, I am Object' + str(count))
        print('==>' + o.getItem('field2'))
    except:
        print('No attribute')
