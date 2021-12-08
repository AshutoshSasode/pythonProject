class Node:
    def __init__(self,key,value):
        self.key,self.value=key,value
        self.next=self.prev=None
class LRU:
    def __init__(self,capacity:int):
        self.cap=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        #left = LRU  right = MRU
        self.left.next,self.right.prev=self.right,self.left

    def remove(self,node):

    def insert(self,node):

    def get(self,key,value)->int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self,key,value)->int:
        if key in self.cache:
            return self.cache[key]
        


