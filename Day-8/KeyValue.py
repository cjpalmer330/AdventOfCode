class KeyValue:

    def __int__(self, key, left, right):
        self.key = key
        self.leftChild = left
        self.rightChild = right

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild
