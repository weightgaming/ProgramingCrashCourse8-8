def bubbleSort(collection: list):
    isListSorted: bool = False
    while not isListSorted:
        isListSorted = True

        for x in range(1, len(collection)):
            if collection[x - 1] > collection[x]:
                smaller = collection[x]
                larger = collection[x - 1]

                collection[x] = larger
                collection[x - 1] = smaller

                isListSorted = False


if __name__ == '__main__':
    randomList: list = [2, 5, 12, 45, 2, 1]

    print(randomList)
    bubbleSort(randomList)
    print(randomList)