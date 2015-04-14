class Class(object):

    def __init__(self, a):
        self.OurAttr = a

    @property
    def OurAttr(self):
        return self.__OurAttr

    @OurAttr.setter
    def OurAttr(self, a):
        if a < 0:
            self.__OurAttr = 0
        elif a > 1000:
            self.__OurAttr = 1000
        else:
            self.__OurAttr = a


print(Class(-2).OurAttr)
print(Class(1002).OurAttr)
print(Class(3).OurAttr)

