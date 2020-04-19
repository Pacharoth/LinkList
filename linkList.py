class Menu:
    print ('\t\t===========================')
    print ('\t\t+Welcome to Link list -__-+')
    print ('\t\t===========================\n')
    print ('1.Set begin of linklist.\n')
    print ('2.Set the end of linklist.\n')
    print ('3.Delete Begin.\n')
    print ('4.Delete End.\n')
    print ('5.Search List.\n')
    print ('6. Show List.\n')
    print ('7. Exit the program.\n')

class Node:
    #struct element create data set as val and 
    #next as None when no data 
    def __init__(self,val):
        self.data = val
        self.next = None
    def getData(self):
        return self.getData
    def getNext(self):
        return self.next
    def setData(self,val):
        self.data=val
    def setNext(self,val):
        self.next=val

class linkList:
    #start create struct element
    def __init__(self):
        self.head = None
        self.tail = None
        self.n=0
    #create empty list
    def isEmpty(self):
        self.n=0
        return self.head is None,self.tail is None,self.n
    #add the begin
    def addBegin(self,item):
        new_element = Node(item)#set in function node
        new_element.setNext(self.head)
        self.head =new_element
        if self.n==0:
            self.tail=new_element
        self.n += 1
    #end list
    def endList(self,item):
        new_element=Node(item)
        if self.n==0:
            self.addBegin(item)
        else:
            tail= self.tail
            new_element.setNext(None)
            tail.setNext(new_element)
            self.tail=new_element
            self.n +=1
    #delete head
    def deleteBegin(self):
        if self.n==0:
            print("Cant delete")
        else:
            tmp = self.head
            self.head = tmp.getNext()
            tmp = None
            if self.n==1:
                self.tail = None
            self.n -=1
            print("delete successful")
    #delete end of list
    def deleteEndList(self):
        if self.n==0:
            print("Bro you cant delete")
        else:
            if self.n==1:
                self.deleteBegin()
            else:
                tmp =self.head
                for i in range(0,self.n-2):
                    tmp =tmp.getNext()
                self.tail=tmp
                tail=self.tail
                tail.setNext(None)
                tmp =None
                self.n -=1
                print("Delete successful")
    #search list
    def searchLinkList(self,item):
        count=0
        tmp = Node(item)
        tmp=self.head
        while tmp is not None:
            if tmp.data is item:
                print (tmp.data)
                tmp=tmp.getNext()
                count+=1
            else:
                tmp=tmp.getNext()
        print ('The result of {} is {}'.format(item,count))
    def showAll(self):
        tmp =self.head
        while tmp is not None:
            print (tmp.data)
            tmp = tmp.next
f = linkList()
while(1):
    p=Menu()
    choice=int(input("Choice:"))
    #add Begin
    if choice==1:
        num = int(input("Input the number:"))
        f.addBegin(num)
    #add end
    elif choice ==2:
        num = int(input("Input the number:"))
        f.endList(num)
    #delete Begin
    elif choice==3:
        f.deleteBegin()
    #delete end of list
    elif choice==4:
        f.deleteEndList()
    #search list
    elif choice==5:
        num = int(input("Search number of Data:"))
        f.searchLinkList(num)
    #show all
    elif choice == 6:
        f.showAll()
    #Exit the Program
    elif choice==7:
        print ('Exit the program')
        break

