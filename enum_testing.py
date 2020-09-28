from enum import Enum, auto

class Sequences(Enum): # Создаем класс Sequences, родительским классом
    list = 1           # которого является класс Enum
    tuple = 2
    dict = 3

class Status(Enum):
    new = auto() #автоматически присваивает элементу значение “1”,
                 #а каждому последующему — значение на единицу больше
    waiting = auto() #1+1=2
    assigned = auto() #2+1=3
    completed = auto()
    failed = auto()

class Color(Enum):
    BLUE = 1
    BLACK = 2
    BROWN = 3

class Students(Enum):
    IGOR = 1
    SERGEY = 2
    VASYA = 3
    def info(self):
        print(f"Имя - {self.name}, значение - {self.value}")

class PigeonState(Enum):
    eating = (0, "Ест")
    sleeping = (1, "Спит")
    flying = (2, "Парит в небесах")

    def __init__(self, id, title):
        self.id = id
        self.title = title

print(Sequences.list) # выводим значения
print(Sequences.tuple.name)
print(Sequences.dict.value)

for s in Status: #Перечисления — это итерируемые объекты
    print(s)
    print(type(s)) #Тип элемента перечисления — это перечисление

#Элементы перечисления хэшируемые. Можно использовать их в словарях и множествах.
apples = {}
apples[Color.BLUE] = 'blue'
apples[Color.BLACK] = 'black'
print(apples)

#Можно добавлять методы к перечислениям
Students.IGOR.info()

print(PigeonState.flying.id)
print(PigeonState.flying.title)
