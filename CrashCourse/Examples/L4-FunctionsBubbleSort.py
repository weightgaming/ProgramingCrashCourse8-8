def bubbleSort(collection: list):
    isListSorted: bool = False
    while not isListSorted:
        isListSorted = True
        for index in range(1, len(collection)):
            if collection[index-1] > collection[index]:
                smaller: int = collection[index]
                larger: int = collection[index-1]

                collection[index] = larger
                collection[index-1] = smaller
                isListSorted = False


if __name__ == '__main__':
    randomList: list = [2, 5, 12, 45, 2, 1]

    print(randomList)
    bubbleSort(randomList)
    print(randomList)