from collections import *
from itertools import *

class Stack(object):

    def __init__(self, iterable=None):
        self.__myCon = list() if iterable == None else list(iterable)

    def push(self, item):
        self.__myCon.append(item)

    def pop(self):
        return self.__myCon.pop()

    def peek(self):
        return self.__myCon[len(self.__myCon)-1]

    def isEmpty(self):
        return not bool(len(self.__myCon))

    def size(self):
        return len(self.__myCon)

    def debug(self):
        return self.__myCon


def parChecker(string):
    stack1 = Stack()
    stack2 = Stack()
    
    for letter in string:
        if letter == "(":
            stack1.push(letter)
        else:
            if stack1.isEmpty():
                return False
            else:
                stack2.push(letter)
                
    return stack2.size() == stack1.size()

def allChecker(string):
    opener = list()
    closer = list()
    open_chars = "({["
    close_chars = ")}]"
    
    for l in string:
        if l in open_chars:
            opener.append(l)
        else:
            closer.append(l)

    d1 = dict(Counter(opener))
    d2 = dict(Counter(closer))

    for k1, k2 in product(open_chars, close_chars):
        if k1 not in d1:
            d1[k1] = 0
        elif k2 not in d2:
            d2[k2] = 0
        elif d1[k1] != d2[k2]:
            return False

    return True
    
    
def main():
    print(allChecker('((()))'))
    print(allChecker('(()'))
    print(allChecker('{{([][])}()}'))
    print(allChecker('[{()]'))
    print(allChecker('(((]]]'))
    

if __name__ == "__main__":
    main()
    
        
