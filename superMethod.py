class person(object):
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(self.name)
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def disp1(self):
        super().disp()
        return self.rno
name=str(input("Enter your name:"))
rno=int(input("Enter your roll no.:"))
s1=student(name,rno)
print(s1.disp1())