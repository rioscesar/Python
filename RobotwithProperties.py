class Robot(object):

    def __init__(self, name, build, lk = 0.5, lp = 0.5):
        self.name = name
        self.build = build
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
