import unittest
import brackets
import os

'''def processFile(filePath)

def runTests(dirPath)

	foreach input, output in dirPath()
		actual = processFile(input)
		expected = load(output)
		Compare(actual, expected)


def Compare(expected, actual)

def load(filePath)
'''

bracketTestFolder = r"C:\Users\achyu\OneDrive\Desktop\week1_basic_data_structures\1_brackets_in_code\tests"
os.chdir(bracketTestFolder)

def load(filePath):
        with open(filePath, 'r') as f:
            return f.read()
        
testList = []
evalList = []
for file in os.listdir():
    if file.endswith(".a"):
        filePath = f"{bracketTestFolder}\{file}"
        evalList.append(filePath)
    else:
        filePath = f"{bracketTestFolder}\{file}"
        testList.append(filePath)
class TestBrackets(unittest.TestCase):
    
        def testBrackets(self):
            testLength = len(testList)
            for i in range(testLength):
                testValue = brackets.find_mismatch(load(testList[i])).lower()
                evalValue = load(evalList[i]).lower().rstrip()
                self.assertEqual(testValue, evalValue)

if __name__ == '__main__':
    unittest.main()    
