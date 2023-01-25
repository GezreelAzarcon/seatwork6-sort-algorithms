from sortAlgorithms import selectionSort
from sortAlgorithms import bubbleSort
from sortAlgorithms import insertionSort
from sortAlgorithms import mergeSort
from sortAlgorithms import quickSort

myArray1 = [45, 55, 57, 17, 23, 19, 73, 92, 60, 26]
myArray2 = [45, 55, 57, 17, 23, 19, 73, 92, 60, 26]
myArray3 = [45, 55, 57, 17, 23, 19, 73, 92, 60, 26]
myArray4 = [45, 55, 57, 17, 23, 19, 73, 92, 60, 26]
myArray5 = [45, 55, 57, 17, 23, 19, 73, 92, 60, 26]

selectionSort(myArray1)
bubbleSort(myArray2)
insertionSort(myArray3)
mergeSort(myArray4)
myArray5 = (quickSort(myArray5))

print(myArray1)
print(myArray2)
print(myArray3)
print(myArray4)
print(myArray5)
