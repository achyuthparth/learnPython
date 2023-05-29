def PalindromePermutation(inputString):
    if len(inputString) == 1:
        return True
    dictionary = {}
    for character in inputString:
        if character not in dictionary:
            dictionary[character] = 0
        if character in dictionary:
            dictionary[character] += 1

    if len(inputString) % 2 == 1:   
        oddcheck = 0
        for key in dictionary:
            if dictionary[key] % 2 == 1:
                oddcheck += 1
            if oddcheck >= 2:
                return False     
    
    if len(inputString) % 2 == 0:
        for key in dictionary:
            if dictionary[key] % 2 != 0:
                return False
    
    return True



print(PalindromePermutation("1234 5 4321"))