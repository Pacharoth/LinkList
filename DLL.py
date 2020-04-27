#create the Menu to choose create the program
class Menu:
	def menuMain():
		print('\t==========================================')
		print('\t+\t\t===================                 +')
		print('\t+\t\t+Welcome to DLL-_-+                 +')
		print('\t+\t\t===================                 +')
		print('\t==========================================')
		print('\t+1.Insert Begin\t+2.Insert End of List+')
		print('\t==========================================')
		print('\t+3.Delete Begin\t+4.Delete End 	 +')
		print('\t+5.Show Begin  \t+5.Show End		 +')
		print('\t==========================================')
	
	
	
#create the structure of the list DLL
class Node:
	def __init__(self,val):
		self.data = val
		self.next = None
		self.prev= None
	#get the data 
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def getPrev(self):
		return self.prev
	def setData(self,val):
		self.data= val
	def setNext(self,val):
		self.next = val
	def setPrev(self,val):
		self.prev = val
#create list and function of connection
p= Menu()
p.menuMain()
