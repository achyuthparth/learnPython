import math


def searchBetween(startIndex, endIndex, numToFind, array):
    # handle start == end
    # dont need ^

    # handle start > end
    # not possible ^

    mid = (endIndex + startIndex) // 2
    
    if numToFind == array[mid]:
        return numToFind
    if numToFind < array[mid] and numToFind > array[mid - 1]:
        return array[mid]
    if array[startIndex] >= numToFind:
        return array[startIndex]
    if array[endIndex] <= numToFind:
        return array[endIndex] # perhaps return None here?
    if array[mid] > numToFind:
        mid = mid // 2
        return searchBetween(startIndex, mid, numToFind, array)
    if array[mid] < numToFind:
        mid += mid //2
        return searchBetween(mid, endIndex, numToFind, array)


def oneUp(numList, num):
    numList.sort()
    print((numList.__len__() - 1))

    #numFound = False
    #searchIndex = (numList.__len__() - 1) // 2

    result = searchBetween(0, len(numList) -1, num, numList)
    return result

    # while (numFound == False):
        
    #     if (num == numList[searchIndex]):
    #         return num
    #     if (num < numList[searchIndex] and num > numList[searchIndex - 1]):
    #         return numList[searchIndex]

    #     if numList[0] >= num:
    #         return numList[0]
    #     if (numList[numList.__len__() - 1]) <= num:
    #         return numList[numList.__len__() - 1]


    #     mid = searchIndex // 2
    #     if (numList[searchIndex] > num):
    #         searchIndex = mid
    #     if (numList[searchIndex] < num):
    #         searchIndex += mid
        




def RunTest(list, inputNum, expectedValue):
    result = oneUp(list, inputNum)
    print(str(result) + " " + str(result == expectedValue))

sampleList = [3, 4, 9, 10, 12, 13]
sampleOdd = [3, 4, 9, 11, 14]

RunTest(sampleList, 2, 3)
RunTest(sampleList, 16, 13)
RunTest(sampleList, 9, 9)
RunTest(sampleList, 13, 13)
RunTest(sampleList, 3, 3)
RunTest(sampleOdd, 2, 3)
RunTest(sampleOdd, 16, 14)
RunTest(sampleOdd, 9, 9)
RunTest(sampleOdd, 14, 14)
RunTest(sampleOdd, 3, 3)
RunTest(sampleList, 11, 12)
RunTest(sampleOdd, 11, 11)
RunTest(sampleOdd, 13, 14)



