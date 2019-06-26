#Есть класс "Воин". От него создаются два экземпляра-юнита.
#Каждому устанавливается здоровье в 100 очков.
#В случайном порядке они бьют друг друга.
#Тот, кто бьет, здоровья не теряет.
#У того, кого бьют, оно уменьшается на 20 очков от одного удара.
#После каждого удара надо выводить сообщение, какой юнит атаковал,
#и сколько у противника осталось здоровья.
#Как только у кого-то заканчивается ресурс здоровья,
#программа завершается сообщением о том, кто одержал победу.
from random import shuffle

class Warrior:
    helth = 100
    def setName(self, n):
        self.name = n
    def getName(self):
        try:
            return self.name
        except:
            return 'NoName'
    def hitEnemy(self, damage=20):
        return damage

fw = Warrior()
sw = Warrior()
fw.setName(input('First warrior name:'))
sw.setName(input('Second warrior name:'))
battle = [fw, sw]
while battle[0].helth>0:
    shuffle(battle)
    battle[0].helth -= battle[1].hitEnemy()
    print(battle[0].getName() + ' attacked by ' + battle[1].getName())
    print(fw.getName() + ' (' + str(fw.helth) +') - ' + sw.getName() + ' (' + str(sw.helth) +')')
print('Winner is '+battle[1].getName())
