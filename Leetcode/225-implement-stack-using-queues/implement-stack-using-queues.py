class MyStack(object):

    def __init__(self):
        self.q=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

    def pop(self):
        """
        :rtype: int
        """
        return self.q.pop(0)
    def top(self):
        """
        :rtype: int
        """
        return self.q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q)==0 :
            return True
        else :
            return False        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()