class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory(object):

    #                                   c
    # [home -> leetcode -> apple ->- facebook]
    #                            

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = Node(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        x = 0
        while self.curr and self.curr.prev and x < steps:
            self.curr = self.curr.prev
            x += 1
        return self.curr.url

        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        x = 0
        while self.curr and self.curr.next and x < steps:
            self.curr = self.curr.next
            x += 1
        return self.curr.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)