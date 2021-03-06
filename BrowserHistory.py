"""
Question:
You have a browser where you start on the homepage and you can visit another url, 
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(str homepage) 
    Initializes the object with the homepage of the browser.
    
void visit(str url) 
    Visits url from the current page. 
    
string back(int steps) 
    Move "steps" back in history. Return the url after moving
    
string forward(int steps) 
    Move "steps" forward in history. Return the url after moving


Example 1:
obj = BrowserHistory("A")
obj.visit("B")
obj.visit("C")
print(obj.back(2))  # A
print(obj.forward(1))  # B


Example 2:
obj = BrowserHistory("A")
obj.visit("B")
obj.visit("C")
print(obj.back(1))  # B
print(obj.back(1))  # A
obj.visit("D")
print(obj.forward(1))  # D
print(obj.forward(1))  # D


Notes:
- steps can be larger than history list
- visit() clears up all the forward history.
- can be implemented with stack + pointer or doubly linked list
- simpler version: assume steps is always 1
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
