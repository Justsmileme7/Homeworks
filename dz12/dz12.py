class Moving:

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
    def __init__(self):
        self.is_engine_work = False

    def move(self):
        if self.is_engine_work:
            print('Car ride')
        else:
            print('Please launch the car')

    def launch(self):
        if self.is_engine_work:
            print('Car is already started')
        else:
            self.is_engine_work = False
            print('Car is working')


for ob in (Duck(), Tiger()):
    ob.voice()
    ob.move()

duck = Duck()
duck.move()
tiger = Tiger()
tiger.move()
tiger.voice()
bmv = Car()
bmv.move()
bmv.launch()
