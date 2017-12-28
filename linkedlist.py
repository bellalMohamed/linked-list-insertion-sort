import random
import time

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    # add item to linked list
    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    # display the linked list
    def display(self):
        elements = []
        currentNode = self.head

        while currentNode != None:
            elements.append(currentNode.data)
            currentNode = currentNode.next

        print(elements)

    # add node to sorted linked list
    def addToSorted(self, node):
        previousNode = None
        currentNode = self.head

        while currentNode != None:
            if currentNode.data > node.data:
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next

        if previousNode == None:
            node.next = currentNode
            self.head = node
        else:
            previousNode.next = node
            node.next = currentNode

    # this is the first sorting algoritm testing it's slower that the second algorithm.
    # basically this algorithm excludes the node needs to be sorted from the linked list 
    # and re-inject it into the linked list in the suitable place
    def sort(self):
        start = time.time()
        insertionPointer = self.head
        while insertionPointer.next != None:
            if insertionPointer.data > insertionPointer.next.data:
                tempNode = insertionPointer.next
                insertionPointer.next = insertionPointer.next.next
                self.addToSorted(tempNode)
            else:
                insertionPointer = insertionPointer.next

        end = time.time()
        print(end - start)


# this is the second sorting algorithm it's simply created another empty linked list and consider at
# as a sorted linked list and clone every node from the not sorted linked list and inject it to the linked
# list using the `addToSorted` Function.
# It's faster algorithm, but it needs more memory. but this issue can be solved by destructing the old linked list or re-assign
# old linked list to the new sorted one them destructing the new linked list.
def sortLinkedListAlg2(alist):
    start = time.time()

    insertionPointer = alist.head

    sortedList = LinkedList()
    while insertionPointer != None:
        theNode = insertionPointer
        insertionPointer = insertionPointer.next
        sortedList.addToSorted(theNode)

    end = time.time()
    print("List: ", end - start)

# array insertion sort algorithm
def sortArray(alist):
    start = time.time()

    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
            alist[position] = currentvalue

    end = time.time()
    print("Array: ", end - start)




myList = LinkedList()
myArray = []

# Create random ints and adding them to the array and the linked list
for x in range(1, 1000):
    myInt = random.randint(0, 20000)
    myList.add(myInt)
    myArray.append(myInt)

sortLinkedListAlg2(myList) #calling insertion sort on the linked list
sortArray(myArray) # calling insertion sort on the array