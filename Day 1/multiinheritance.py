class father:
    fname=''
    def display(self):
        print(self.fname)

class mother:
    mname=''
    def display(self):
        print(self.mname)

class son(father):
    sname=''
    def sdisplay(self):
        print("son name is:", self.sname)
        print('father name is:', self.fname)
        print('mother name is:', self.mname)

s=son()
s.fname='devraj'
s.sname='sudyumna'
s.mname='devika'
s.sdisplay()
