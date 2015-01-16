class Node(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value


class BST(object):

    def __init__(self, root):
        self.__root = Node(root)

    def put(self, value):
        if self.__root.right == None:
            self.__root.right = Node(value)
        else:
            tmp = self.__root
            prev = None
            direction = None
            while tmp != None:
                if value > tmp.value:
                    prev, tmp = tmp, tmp.left
                    direction = "left"
                elif value < tmp.value:
                    prev, tmp = tmp, tmp.right
                    direction = "right"
                else:
                    return False
            if direction == "left":
                prev.left = Node(value)
            elif direction == "right":
                prev.right = Node(value)

    def search(self, value):
        tmp = self.__root
        while tmp != None or tmp.value != None:
            if value > tmp.value:
                tmp = tmp.left
            elif value < tmp.value:
                tmp = tmp.right
            else:
                return True
        return False

    def delete(self, value):
        if self.__root.value == value:
            self.__root.value = Node(None)
            return True
        tmp = self.__root
        while tmp != None:
            if value > tmp.value:
                tmp = tmp.left
            elif value < tmp.value:
                tmp = tmp.right
            else:
                if tmp.right == None and tmp.left == None:
                    tmp = None
                    return True
                elif tmp.right == None:
                    tmp = tmp.left
                    return True
                elif tmp.left == None:
                    tmp = tmp.right
                    return True
                else:
                    tmp, tmp.left.right = tmp.left, tmp.right
                    return True
        return False

    def debug(self, value):
        tmp = self.__root
        while tmp != None:
            if value > tmp.value:
                print(str(tmp.value).ljust(3, " "))
                i+=1
                tmp = tmp.left
            elif value < tmp.value:
                print(str(tmp.value).rjust(3, " "))
                tmp = tmp.right
            else:
                print(str(tmp.value))
                return 
            
                
                

x = BST(3)
print(x.delete(3))
print(x.search(3))
                    
        
        
           

























        
