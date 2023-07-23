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
            return f.read().rstrip()
        
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
                testValue = brackets.find_mismatch(load(testList[i]))
                evalValue = load(evalList[i])
                if testValue != evalValue:
                    print(i)
            self.assertEqual(testValue, evalValue)

        def test13(self):
            testValue = brackets.find_mismatch(load(testList[13]))
            evalValue = load(evalList[13])
            self.assertEqual(testValue, evalValue)
            #works
        def test15(self):
            testValue = brackets.find_mismatch(load(testList[15]))
            evalValue = load(evalList[15])
            self.assertEqual(testValue, evalValue)
            #works
        def test17(self):
            testValue = brackets.find_mismatch(load(testList[17]))
            evalValue = load(evalList[17])
            self.assertEqual(testValue, evalValue)
            #works
        
        def test25(self):
            testValue = brackets.find_mismatch(load(testList[25]))
            evalValue = load(evalList[25])
            self.assertEqual(testValue, evalValue)
            
        
        def test26(self):
            testValue = brackets.find_mismatch(load(testList[26]))
            evalValue = load(evalList[26])
            self.assertEqual(testValue, evalValue)
            
        def test28(self):
            testValue = brackets.find_mismatch(load(testList[28]))
            evalValue = load(evalList[28])
            self.assertEqual(testValue, evalValue)
        #works
        
if __name__ == '__main__':
    unittest.main()    
