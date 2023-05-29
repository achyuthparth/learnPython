def StringRotation(string1, string2):
    if len(string1) != len(string2):
        return False
    for character in string1:
        if character not in string2:
            return False
        #first, find the index of character in string2
        #if next character is not the same, then check if it is the first one, if not, then return false
        if string1.index(character) == len(string1) - 1:
            next1 = string1[0]
        else: 
            next1 = string1[string1.index(character) + 1]
        
        if string2.index(character) == len(string2) - 1:
            next2 = string2[0]
        else: 
            next2 = string2[string2.index(character) + 1]

        if next1 != next2:
            if character != string2[0]:
                return False
    return True

print(StringRotation("act", "tac"))
#how do i find the exact index instead of finding only the first one?
print(StringRotation("bottlewater", "waterbottle"))