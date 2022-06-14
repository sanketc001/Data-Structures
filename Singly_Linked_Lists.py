class Element():
    def __init__(self,key,pred):
        self.pred=pred
        self.key=key
class Mylist():
    def __init__(self,head):
        self.head=head
    def insert(self, k):
        element = Element(k, None)
        if self.head == None:
            self.head = element
        else:
            element.pred = self.head
            self.head = element
    def insert1(self,k,s):
        element = Element(k, s,s.pred)
        if self.head == None:
            self.head = element
        else:
            element.pred = self.head
            self.head = element
    def search(self,s):
        var = self.head
        while var != None and var.key != s:
            var = var.pred
        return var
    def delete(self,d):
        var=list.search(d)
        if var!=None:
            print(var.key," Deleted.")
            var.key=None
        else:
            print("No Entries.")



list=Mylist(None)
list.insert(9)
list.insert(8)
list.insert(7)
list.insert(6)
list.insert(4)
print(list.search(8).key)
list.delete(7)
var=list.head
for i in range(0,5):
    if var==None or var.key==None:
        var= var.pred
    else:
        print(var.key)
        var=var.pred
list.insert1(5,6)