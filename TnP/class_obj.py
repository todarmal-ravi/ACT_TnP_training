class human:
    def birth(self,gender): # referrence of object that is used to call the function
        self.__gender=gender
        print(id(self))
    def naming(self,name): #will always have to use 'self.' for variables
        self.__name=name
    def intro(self):
        print(self.__gender,self.__name)

h=human() #object creation
h.birth("male") #calling
h.naming("malrfr")
h.intro()