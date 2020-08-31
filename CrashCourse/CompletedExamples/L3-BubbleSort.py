# Bubble Sort

if __name__ == '__main__':
    randomList: list = [2, 5, 12, 45, 2, 1]

    print(randomList)

    isListSorted: bool = False
    while not isListSorted:
        isListSorted = True

        for x in range(1, len(randomList)):
            if randomList[x-1] > randomList[x]:
                smaller = randomList[x]
                larger = randomList[x-1]

                randomList[x] = larger
                randomList[x-1] = smaller

                isListSorted = False

    print(randomList)
