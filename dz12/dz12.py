class Moving:
    def __int__(self):
        self.name = name

    def move(self):
        raise NotImplementedError('Somethig wrong')


class Animal(Moving):
    def voice(self):
        raise NotImplementedError('Somethig wrong 1')


class Transport(Moving):
    def launch(self):
        raise NotImplementedError('Somethig wrong 2')


class Duck(Animal):
    def voice(self):
        print('qwa-qwa')

    def move(self):
        print('swim')


class Tiger(Animal):
    def voice(self):
        print('rrrrrr')

    def move(self):
        print('run')

class Car(Transport):
    def move(self):
        print('drive')
    def launch(self):
        print('start')

duck = Duck()
duck.move()
tiger = Tiger()
tiger.move()
bmv = Car()
bmv.move()
