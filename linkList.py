class Menu:
    print '\t\t==========================='
    print '\t\t+Welcome to Link list -__-+'
    print '\t\t===========================\n'
    print '1.Set begin of linklist.\n'
    print '2.Set the end of linklist.\n'
    print '3.Delete Begin.\n'
    print '4.Delete End.\n'
    print '5.Delete Begin.\n'
    print '6.Search List.\n'
    print '7. Show List.\n'
    print '8. Exit the program.\n'

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
    def size(self):
        count=0
        tmp= self.head
        while tmp is not None:
            count +=1
            tmp = tmp.getNext()
        return count
    def endList(self,item):
        new_element=Node(item)
        current =self.head
        prev= None
        pos=0
        length = self.size()
        while pos < length:
            prev= current
            current = current.getNext()
            pos +=1
        if prev is None:
            current.setNext(self.head)
            self.head=new_element
        else:
            prev.setNext(new_element)
            self.tail=prev
    def searchLinkList(self,item):
        count=0
        tmp = Node(item)
        tmp=self.head
        while tmp is not None:
            if tmp.data is item:
                print tmp.data
                tmp=tmp.getNext()
                count+=1
            else:
                tmp=tmp.getNext()
        print ('The result of {} is {}'.format(item,count))
    def showAll(self):
        tmp =self.head
        while tmp is not None:
            print tmp.data
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
    elif choice==6:
        num = int(input("Search number of Data:"))
        f.searchLinkList(num)
    #show all
    elif choice == 7:
        f.showAll()
    
    elif choice==8:
        print 'Exit the program'
        break

