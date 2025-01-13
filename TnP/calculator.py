class calculator:
    
    def add(self,a,b):
        print(f"{a}+{b} = {a+b}")
    def sub(self,a,b):
        print(f"{a}-{b} = {a-b}")
    def mult(self,a,b):
        print(f"{a}*{b} = {a*b}")
    def divi(self,a,b):
        print(f"{a}/{b} = {a/b}")

obj=calculator()
obj.add(10,20)