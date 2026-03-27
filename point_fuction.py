class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def good(self):
        print(self.x)
        print(self.y)
p1=point(2,3)
print(p1.good())