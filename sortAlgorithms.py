#Selection Sort
def selectionSort(myList):
    for x in range(0, len(myList) - 1):
        minNum = x
        for y in range(x + 1, len(myList)):
            if myList[y] < myList[minNum]:
                minNum = y
        myList[x], myList[minNum] = myList[minNum], myList[x]

#Bubble Sort 
#Insertion Sort 
#Merge Sort
#Quick Sort