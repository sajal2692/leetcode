class BrowserNode:
    
    def __init__(self, page: str, next=None, prev=None):
        self.page = page
        self.next = None
        self.prev = None
        
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = BrowserNode(page=homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        new = BrowserNode(page=url)
        new.prev = self.curr
        self.curr.next = new
        self.curr = new

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.page

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)