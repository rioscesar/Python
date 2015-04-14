class TEST(object):

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        if fname.lower() == "cesar":
            self.__fname = "Jose"
        else:
            self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        if lname.lower() == "rios":
            self.__lname = "Gonzalez"
        else:
            self.__lname = lname



x = TEST("Cesar", "Rios")
print(x.fname)
print(x.lname)
x.lname = "juan"
print(x.lname)
