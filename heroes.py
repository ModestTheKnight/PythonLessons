from random import random, choice

class Warrior:
    def __init__(self, u, c, t):
        self.uid = u
        self.command = c
        print('Generate ' + t +' level 0 ' + str(u) + ' and assighn to command ' + str(c))

class Soldier(Warrior):
    def __init__(self, u, c):
        Warrior.__init__(self, u, c, 'soldier')
    def followHero(self, h):
        self.hero = h
        print('Soldier ' + str(self.uid) + ' follow hero ' + str(h.uid))

class Hero(Warrior):
    def __init__(self, u, c):
        Warrior.__init__(self, u, c, 'hero')
        self.level = 0
    def levelUp(self):
        self.level += 1
        print('Hero ' + str(self.uid) + ' level up to ' + str(self.level)) 

def createUid():
    return round(random()*100000000)

cn = int(input('Enter commands amount: '))
commands = [[] for i in range(cn)]
#generate hero for each command
for i in range(cn):
    commands[i].append(Hero(createUid(),i))
sn = int(input('Enter soldiers amount: '))
#generate soldiers
for _ in range(sn):
    c = choice(range(cn))#random command for soldier
    commands[c].append(Soldier(createUid(),c))
#command list
print ('COMMANDS:')    
for c in commands:
    print([w.uid for w in c])
#determine max command
mc = max([len(x) for x in commands])
for c in commands:
    if len(c) == mc:
        c[0].levelUp()
#follow the leader!
i = 0
while len(commands[i])<mc:
    i += 1
commands[i][choice(range(1,mc))].followHero(commands[i][0])
    
