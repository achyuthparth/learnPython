#find the armstrong numbers between 100 and 1 thousand
#if a number that is equal to the sum of digits raised to the power or number of digits
#153 = 1**3 + 5**3 + 3**3

def Armstrong(start, end):
    while start < end:
        if (int(str(start)[0]) ** 3 + int(str(start)[1]) ** 3 + int(str(start)[2]) ** 3) == start:
            print(start)
        start += 1

def Armstrong2(start, end):
    while start < end:
        sum = 0
        for i in str(start):
            sum += (int(str(start)[i]) ** len(str(start)))
        if sum == start:
            print(start)


Armstrong2(100, 1000)