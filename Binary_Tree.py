class Student():
    def __init__(self,e1,e2,e3,e4,e5,e6):
        self.prn=e1
        self.name=e2
        self.email=e3
        self.age=e4
        self.gender=e5
        self.XIIth_percentage=e6
    def printInfo(self):
        print(self.prn)
        print(self.name)
        print(self.email)
        print(self.age)
        print(self.gender)
        print(self.XIIth_percentage)
        print("##################\n")

class Element():
    def __init__(self,key,left,right,p):
        self.left=left
        self.right=right
        self.p=p
        self.key=key
class Tree():
    def __init__(self,root):
        self.root=root
    def insert(self,x):
        k = Element(x, None, None, None)
        if (self.root == None):
            self.root = k
        else:
            p = self.root
            t = None
            while (p != None):
                t = p
                if (k.key.prn < t.key.prn):
                    p = p.left
                else:
                    p = p.right
            k.p = t
            if (k.key.prn > t.key.prn):
                t.right = k
            else:
                t.left = k

    def search(self,x):
        l=self.root
        p=""
        while(l!=None and l.key.prn!=x):
            if(l.key.prn>x):
                l=l.left
                p="Left"
            else:
                l=l.right
                p="Right"
        return l,p
    def iterate(self,x):
        if (x.left==None and x.right==None):
            return x
        else:
            if (x.left != None):
                self.iterate(x.left)
                print(x.key.prn)
            elif (x.right != None):
                self.iterate(x.right)
                print(x.key.prn)
    def printTree(self):
        print("       ",self.root.key.prn)
        print("   ",self.root.left.key.prn,"     ",self.root.right.key.prn)
        print(" ",self.root.left.left.key.prn," ",self.root.left.right.key.prn," ",self.root.right.left.key.prn," ",self.root.right.right.key.prn)
        print("",self.root.left.left.left.key.prn,"  ",self.root.left.right.right.key.prn,"",self.root.right.left.left.key.prn,"   ",self.root.right.right.right.key.prn)


list=Tree(None)
s1=Student(6,"Sanket","Sanket@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(3,"Human","Human@dypiu.ac.in",18,'B','87')
list.insert(s1)
s1=Student(9,"Barry","Barry@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(2,"      ","      @dypiu.ac.in",18,' ','100')
list.insert(s1)
s1=Student(4,"Emperor","Emperor@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(8,"Shivam","Shivam@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(10,"Sidhant","Sidhant@dypiu.ac.in",18,'M','87')
list.insert(s1)
s1=Student(1,"Boa","Boa@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(5,"Robin","Robin@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(7,"Mai","Mai@dypiu.ac.in",18,'F','87')
list.insert(s1)
s1=Student(11,"Magic","Magic@ddypiu.ac.in",19,' ',"100")
list.insert(s1)
#       6
#    3      9
#  2   4  8   10
# 1     5  7    11
ch=1
while ch!=0:
    ch=int(input(" 1)Insert\n"
                " 2)Print\n"
                " 3)Search\n"
                " 0)Exit\n"))
    if(ch==1):
        i1=int(input("Enter PRN: "))
        i2=input("Enter name: ")
        i3=input("Enter email: ")
        i4=int(input("Enter age: "))
        i5=input("Enter gender")
        i6=int(input("Enter 12th Percentage: "))
        s1=Student(i1,i2,i3,i4,i5,i6)
        list.insert(s1)
    elif(ch==2):
        list.printTree()
    elif(ch==3):
        i1 = int(input("Enter PRN to be searched: "))
        v=list.search(i1)
        if(v[0]==None):
            print("No matching entries.")
        else:
            v[0].key.printInfo()
            print("\nParent ",v[1])
            print(v[0].p.key.prn)

    elif(ch==0):
        break
    else:
        print("Invalid Input!")
# a=[(),(),(),(),(),()]
# print(a[0],"\n",
#     a[],a[2],"\n",
#     a[3],a[4],a[5],a[6],"\n",
#     a[7],a[8],a[9],a[10],a[11],a[12],a[13])