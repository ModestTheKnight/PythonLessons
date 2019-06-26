class Win_Door:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def fullSurface(self):
        return round(2*self.height*(self.width + self.lenght), 2)
    def workSurface(self):
        new_square = self.fullSurface()
        for i in self.wd:
            new_square -= i.square
        return round(new_square, 2)
    def calcRoll(self, w, l):
        roll_square = w * l
        return int(self.workSurface() // roll_square + 1)

r = Room(float(input('Enter room width: ')), float(input('Enter room lenght: ')), float(input('Enter room height: ')))
for i in range (int(input('Enter door num: '))):
    r.addWD(float(input('Enter door' + str(i+1) + ' width: ')), float(input('Enter door' + str(i+1) + ' height: ')))
for i in range (int(input('Enter win num: '))):
    r.addWD(float(input('Enter win' + str(i+1) + ' width: ')), float(input('Enter win' + str(i+1) + ' height: ')))
print('Work surface is: ' + str(r.workSurface()))
print('Num of roll is: ' + str(r.calcRoll(float(input('Enter roll width: ')), float(input('Enter roll lenght: ')))))
