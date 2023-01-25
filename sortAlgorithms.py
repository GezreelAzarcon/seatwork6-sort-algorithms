#Selection Sort
def selectionSort(myList):
    for x in range(0, len(myList) - 1):
        minNum = x
        for y in range(x + 1, len(myList)):
            if myList[y] < myList[minNum]:
                minNum = y
        myList[x], myList[minNum] = myList[minNum], myList[x]

#Bubble Sort 
def bubbleSort(myList):
    sorted = False
    while not sorted:
        sorted = True
        for x in range(0, len(myList) - 1):
            if myList[x] > myList[x + 1]:
                sorted = False
                myList[x], myList[x + 1] = myList[x + 1], myList[x]
    return myList

#Insertion Sort

#Merge Sort

#Quick Sort