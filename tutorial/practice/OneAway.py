def OneAway(inputString1, inputString2):
    letters1 = {}
    letters2 = {}
    if inputString1 == inputString2:
        return True
    if len(inputString2) - 2 >= len(inputString1) or len(inputString1) - 2 >= len(inputString2):
        return False

    for character in inputString1:
        if character not in letters1:
            letters1[character] = 0
        if character in letters1:
            letters1[character] += 1
    
    for character in inputString2:
        if character not in letters2:
            letters2[character] = 0
        if character in letters1:
            letters2[character] += 1
    mismatch = 0
    for character in letters1:
        if character not in letters2:
            mismatch += 1
        if character in letters2:
            if letters1[character] != letters2[character]:
                mismatch += 1
        if mismatch >= 2:
            return False
        
    mismatch = 0    
    for character in letters2:
        if character not in letters1:
            mismatch += 1
        if character in letters1:
            if letters2[character] != letters1[character]:
                mismatch += 1
        if mismatch >= 2:
            return False
    
    return True

print(OneAway("plan", "pan"))
print(OneAway("blade", "parade"))
print(OneAway("fan", "fan"))
print(OneAway("plan", "plane"))
print(OneAway("fan", "fin"))
print(OneAway("fam", "fims"))
