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
def insertionSort(myList):
    for x in range(1, len(myList)):
        toSort = myList[x]
        while myList[x - 1] > toSort and x > 0:
            myList[x], myList[x - 1] = myList[x - 1], myList[x]
            x = x - 1
    return myList

#Merge Sort

#Quick Sort