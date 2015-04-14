class Node(object):

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class UnordedList(object):

    def __init__(self):
        self.head = None
        self.__size = 0

    def add(self, item):
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp
        
        self.__size += 1

    def remove(self, item):
        if self.__size == 0:
            return False
        
        removed = False
        if self.head.data == item:
            self.head = self.head.next
            removed = True
        else:
            slow = self.head
            fast = self.head.next
            while fast != None:
                if fast.data == item:
                    fast = fast.next
                    slow.next = fast
                    removed = True
                    break
                else:
                    fast = fast.next
                    slow = slow.next

        self.__size = self.__size - 1 if removed else self.__size
        return removed

    def size(self):
        return self.__size

    def search(self, item):
        if self.head == None:
            return False
            
        tmp = self.head 

        while tmp != None:
            if tmp.data == item:
                return True
            else:
                tmp = tmp.next

        return False

    def isEmpty(self):
        return self.__size == 0

    def index(self, item):
        count = 0
        found = False

        if self.head == None:
            return -1
        else:
            tmp = self.head
            while tmp != None:
                if tmp.data == item:
                    found = True
                    break
                else:
                    count += 1
                    tmp = tmp.next
                    
        return count if found else -1
                
            
        


if __name__ == "__main__":
    x = UnordedList()
    x.add(3)
    x.add(4)
    x.add(5)
    print(x.index(3))
    print(x.index(4))
    print(x.index(5))

    

            
        
        
                
            
            
                
                
            
