import numpy
class Student():
    def __init__(self,e1,e2,e3,e4,e5,e6):
        self.PRN=e1
        self.name=e2
        self.email=e3
        self.age=e4
        self.gender=e5
        self.XIIth_percentage=e6
    def printInfo(self):
        print(self.PRN)
        print(self.name)
        print(self.email)
        print(self.age)
        print(self.gender)
        print(self.XIIth_percentage)
def ENQUEUE(q,t,h,x):
    if(t==h-1 or t==9 and h==0):
        print("Overflow")
    else:
        if t==9:
            q[t]=x
            t=0
        else:
            q[t]=x
            t=t+1
    return t
def DEQUEUE(q,t,h):
    if(h==t):
        print("Underflow")
        return h,None
    else:
        if h==9:
            temp=q[h]
            q[h]=None
            return 0,temp
        else:
            temp = q[h]
            q[h] = None
            return h+1,temp
tail=0
head=0
studentArray=numpy.empty(10,dtype=object)
print(studentArray)
s1=Student(1,"Sanket","Sanket@dypiu.ac.in",18,'M','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(2,"Human","Human@dypiu.ac.in",18,'B','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(3,"Barry","Barry@dypiu.ac.in",18,'M','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(4,"      ","      @dypiu.ac.in",18,' ','100')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(5,"Emperor","Emperor@dypiu.ac.in",18,'F','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(6,"Shivam","Shivam@dypiu.ac.in",18,'M','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(7,"Sidhant","Sidhant@dypiu.ac.in",18,'M','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(8,"Boa","Boa@dypiu.ac.in",18,'F','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(9,"Robin","Robin@dypiu.ac.in",18,'F','87')
tail=ENQUEUE(studentArray, tail,head, s1)
s1=Student(10,"Mai","Mai@dypiu.ac.in",18,'F','87')
tail=ENQUEUE(studentArray, tail,head, s1)
for i in studentArray:
    if i==None:
        print(None)
    else:
        i.printInfo()
print("Welcome to Queue Implementation on Student Data: ")
ch=-1
while ch!=0:
    ch=int(input("1)Iterate\n"
                " 2)Enqueue\n"
                " 3)Dequeue\n"
                " 0)Exit\n"))
    if(ch==1):
        for i in studentArray:
            if i == None:
                print(None)
            else:
                i.printInfo()
    elif(ch==2):
        i1=int(input("Enter PRN: "))
        i2=input("Enter name: ")
        i3=input("Enter email: ")
        i4=int(input("Enter age: "))
        i5=input("Enter gender")
        i6=int(input("Enter 12th Percentage: "))
        s1=Student(i1,i2,i3,i4,i5,i6)
        tail=ENQUEUE(studentArray, tail,head, s1)
    elif(ch==3):
        head,v=DEQUEUE(studentArray,tail,head)
        if(v==None):
            continue
        else:
            v.printInfo()
    elif(ch==0):
        break
    else:
        print("Invalid Input!")