import math


def oneUp(numList, num):
    orderList = numList.sort()

    numFound = False
    searchIndex = len(orderList) // 2



    while (numFound == False):
        
        if (num == orderList(searchIndex)):
            return num
            
        if (num < orderList(searchIndex) and num > orderList(searchIndex) - 1):
            return orderList(searchIndex)
            




        mid = searchIndex // 2
        if (orderList(searchIndex) < num):
            searchIndex = mid
        if (orderList(searchIndex) > num):
            searchIndex += mid
        
sampleList = list([3, 4, 9, 10, 12, 13])
print(oneUp(sampleList, 6))