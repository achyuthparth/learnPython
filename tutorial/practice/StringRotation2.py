def StringRotation(string1, string2):
    if len(string1) == len(string2):
        if string2 in string1 + string1:
            return True
        return False


print(StringRotation("bottlewater", "waterbottle"))