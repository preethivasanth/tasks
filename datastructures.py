os=['windows7','windows8']
mobile.insert(2,'windowsxp')
top=os[0];
print(os)
dict={1:"int",2:"char",3:"float"}
print(dict[2])
for i in dict:
	print(i)
class Queue:
	    def __init__(self):
	        self.items = []
	
	    def isEmpty(self):
	        return self.items == []
	
	    def enqueue(self, item):
	        self.items.insert(0,item)
	
	    def dequeue(self):
	        return self.items.pop()
	
q=Queue()
q.isEmpty()
q.enqueue('abc')
q.enqueue('write')
q.dequeue()
q=Queue()
q.isEmpty()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
