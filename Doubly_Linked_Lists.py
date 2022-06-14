class Student():
    def __init__(self,e1,e2,e3,e4,e5,e6):
        self.PRN=e1
        self.name=e2
        self.email=e3
        self.age=e4
        self.gender=e5
        self.XIIth_percentage=e6
    def printInfo(self):
        print(self.PRN,self.name,self.email,self.age,self.gender,self.XIIth_percentage,end="")
        print("##################\n")
class Element():
    def __init__(self,key,pred,succ):
        self.pred=pred
        self.succ=succ
        self.key=key
class Mylist():
    def __init__(self,head,tail):
        self.head=head
        self.tail=tail
    def insert(self, k):
        element = Element(k, None, None)
        if self.head == None:
            self.head = element
            self.tail=element
        else:
            self.head.succ = element
            element.pred = self.head
            self.head = element
            self.head.succ=self.tail
            self.tail.pred=self.head
    def search(self,s):
        var = self.head
        c=0
        temp=None
        while var !=self.head and var!=None or c==0 and var!=None:
            if(var.key.PRN==s):
                temp=var
                break
            else:
                var = var.pred
                c=1
        return temp
    def delete(self,d):
        var=list.search(d)
        if var!=None:
            print(var.key.name," Deleted.")
            if (var == self.head and var == self.tail):
                var = None
                self.head=None
                self.tail=None
            elif var.succ!=self.tail and var.pred!=self.head:
                var.pred.succ=var.succ
                var.succ.pred=var.pred
            elif(var.succ==self.tail):
                self.head=var.pred
                var.pred.succ=self.tail
                var.succ.pred=self.head
            elif(var.pred==self.head):
                self.tail=var.succ
                var.succ.pred=self.head
                var.pred.succ=self.tail
        else:
            print("No Entries.")
    def iterate(self):
        x=self.head
        if(x==None):
            print(None)
        else:
            while(self.tail!=x):
                x.key.printInfo()
                x=x.pred
            self.tail.key.printInfo()
list=Mylist(None,None)
s1=Student(1,"Sanket","Sanket@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(2,"Human","Human@dypiu.ac.in",18,'B','87')
list.insert(s1)
s1=Student(3,"Barry","Barry@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(4,"      ","      @dypiu.ac.in",18,' ','100')
list.insert(s1)
s1=Student(5,"Emperor","Emperor@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(6,"Shivam","Shivam@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(7,"Sidhant","Sidhant@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(8,"Boa","Boa@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(9,"Robin","Robin@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(10,"Mai","Mai@dypiu.ac.in",18,'F','87')
list.insert(s1)
print("Welcome to Circular Linked Lists Implementation on Student Data: ")
ch=-1
while ch!=0:
    ch=int(input(" 1)Iterate\n"
                " 2)Insert\n"
                " 3)Delete\n"
                " 4)Search\n"
                " 5)Demonstrate\n"
                " 0)Exit\n"))
    if(ch==1):
        if(list.head==None):
            print("List is Empty.")
        else:
            list.iterate()
    elif(ch==2):
            i1=int(input("Enter PRN: "))
            i2=input("Enter name: ")
            i3=input("Enter email: ")
            i4=int(input("Enter age: "))
            i5=input("Enter gender")
            i6=int(input("Enter 12th Percentage: "))
            s1=Student(i1,i2,i3,i4,i5,i6)
            list.insert(s1)
    elif(ch==3):
        i1 = int(input("Enter PRN to be deleted: "))
        list.delete(i1)
    elif(ch==4):
        i1 = int(input("Enter PRN to be searched: "))
        v=list.search(i1)
        if(v==None):
            print("No matching entries.")
        else:
            v.key.printInfo()
    elif(ch==5):
        if(list.head==None and list.tail==None):
            print("List is Empty")
        else:
            list.head.succ.key.printInfo()
            list.tail.pred.key.printInfo()
    elif(ch==0):
        break
    else:
        print("Invalid Input!")