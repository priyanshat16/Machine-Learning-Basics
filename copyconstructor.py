class rectangle:
    def __init__(self):
        self.l=2
        self.b=3
    def calc_area(self,r):
        print(r.l*r.b)
        print(self.l)
        print(self.b)


a = rectangle()
b = rectangle()
b.calc_area(a)
