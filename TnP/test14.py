# create class human stores name, age, gender
# methods to set details and print
# additional method called eval(): will create vote if >=18, will create play if <18
#this will be stored in todo variable

class human :
    
    n2=0 #class variable, global

    def set(self,name,gender,age): #local variables
        self.name=name #self.<variable> is instance variable, exists for only object
        self.gender=gender
        self.age=age
        self.eval()
        print(f"name:{name} gender:{gender} age:{age} todo:{self.__todo}")

    def eval(self):
        if self.age<18:
            self.__todo="play"
        else:
            self.__todo="vote"

h=human()
h.set("rrr","M",8)