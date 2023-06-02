# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    bracketStack = []
    pos = 1
    for char in text:
        if char in "([{":
            bracketStack.insert(0, char)
        if char in ")]}":
            if bracketStack!= []:
                if char == ")":
                    if bracketStack[0] == "(":
                        del bracketStack[0]
                    else: return str(pos)
                elif char == "]":
                    if bracketStack[0] == "[":
                        del bracketStack[0]
                    else: return str(pos)
                elif char == "}":
                    if bracketStack[0] == "{":
                        del bracketStack[0]
                    else: return str(pos)
            else: return str(pos)
        pos += 1
    return str(pos) if bracketStack != [] else "success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()