"""
Question:

You have a browser of one tab where you start on the homepage and you can visit another url, 
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) 
    Initializes the object with the homepage of the browser.
    
void visit(string url) 
    Visits url from the current page. It clears up all the forward history.
    
string back(int steps) 
    Move steps back in history. 
    If you can only return x steps and steps > x, return only x steps. 
    Return the current url after moving
    
string forward(int steps) 
    Move steps forward in history. 
    If you can only forward x steps and steps > x, forward only x steps. 
    Return the current url after moving
"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = self.furthest = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.curr += 1
        self.furthest = self.curr
        if len(self.history) <= self.curr:
            self.history.append('')
        self.history[self.curr] = url

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.furthest)
        return self.history[self.curr]


obj = BrowserHistory("A")
obj.visit("B")
obj.visit("C")
obj.visit("D")
print(obj.back(1))  # C
obj.visit("E")
print(obj.back(4))  # A
print(obj.forward(2))  # C
print(obj.forward(2))  # E


"""
Simpler Question: Similar to the above question but steps is always 1.
"""

class BrowserHistory:
    def __init__(self, homepage: str):
        self.past = [homepage]
        self.future = []

    def visit(self, url: str):
        self.past.append(url)
        self.future = []

    def back(self) -> str:
        if len(self.past) > 1:
            self.future.append(self.past.pop())
        return self.past[-1]

    def forward(self) -> str:
        if self.future:
            self.past.append(self.future.pop())
        return self.past[-1]


obj = BrowserHistory("A")
obj.visit("B")
obj.visit("C")
print(obj.back())  # B
print(obj.back())  # A
print(obj.forward())  # B
obj.visit("D")
print(obj.back())  # B
print(obj.forward())  # D
print(obj.forward())  # D