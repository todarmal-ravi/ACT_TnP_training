# use class student
# give name, gender but roll number is auto-generated

class student:
    roll_number=0

    def __init__(self,name,gender): #constructor
        self.__name=name
        self.__gender=gender
        student.roll_number+=1
        self.rollno=student.roll_number
        print("roll number:",self.rollno)
    
s=student("rrre","M")