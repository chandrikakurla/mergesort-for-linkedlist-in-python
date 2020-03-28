#node class
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
#linkedlist class
class LinkedList:
	def __init__(self):
		self.head=None
	#creating newnode and  inserting into linkedlist
	def insert(self,newdata):
		newnode=Node(newdata)
		if self.head is None:
			self.head=newnode
			return
		lastnode=self.head
		while True:
			if lastnode.next is None:
				break
			lastnode=lastnode.next
		lastnode.next=newnode
	#printing linkedlist elements
	def printllist(self,head):
		currentnode=self.head
		if currentnode is None:
			print("linkedlist is empty")
			return
		while True:
			if currentnode is None:
				break
			print(currentnode.data)
			currentnode=currentnode.next
	#function for finding mid of linkedlist
	def mid_of_llist(self,head):
		if head is None:
			return head
		slow=head
		fast=head
		while(fast.next is not None and fast.next.next is not None):
			    slow=slow.next
			    fast=fast.next.next
		return slow
	#function for merging two sorted lists
	def sorted_merge(self,left,right):
		temp=None
		if left==None:
			return right
		if right==None:
			return left
		if(left.data<=right.data):
			temp=left
			temp.next=self.sorted_merge(left.next,right)
		else:
			temp=right
			temp.next=self.sorted_merge(left,right.next)
		return temp
    #merge sort 
	def Merge_sort(self,headnode):
		if(headnode is None or headnode.next is None):
			return headnode
		middle=self.mid_of_llist(headnode)
		nexttomiddle=middle.next
		middle.next=None
		left=self.Merge_sort(headnode)
		right=self.Merge_sort(nexttomiddle)
		sortedlist=self.sorted_merge(left,right)
		return sortedlist

if __name__=='__main__':
	llist=LinkedList()
	llist.insert(15)
	llist.insert(12)
	llist.insert(11)
	llist.insert(10)
	llist.insert(5)
	llist.insert(2)
	print("linkedlist before sorting:")
	llist.printllist(llist.head)
	llist.head=llist.Merge_sort(llist.head)
	print("linkedlist after sorting:")
	llist.printllist(llist.head)
	

	
	

