class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        self.scales = True
        super().__init__()

    def swim(self):
        print("Moving in water")

    def breathe(self):
        super().breathe()
        print("Doing this underwater")


bear = Animal()
bear.breathe()
print(bear.num_eyes)

nemo = Fish()
print(nemo.scales)
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)