if __name__ == "__main__":
    randomList: list = [2, 5, 12, 45, 2, 1]

    print(randomList)

    isListSorted: bool = False
    while not isListSorted:
        isListSorted = True

        for index in range(1, len(randomList)):
            if randomList[index-1] > randomList[index]:
                smaller: int = randomList[index]
                larger: int = randomList[index-1]

                randomList[index] = larger
                randomList[index-1] = smaller

                isListSorted = False

    print(randomList)