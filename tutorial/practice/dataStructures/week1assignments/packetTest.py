import unittest
import packets
import os

packetTestFolder = r"C:\Users\achyu\OneDrive\Desktop\week1_basic_data_structures\3_network_simulation\tests"
os.chdir(packetTestFolder)

def load(filePath):
        with open(filePath, 'r') as f:
            return f.read()
        
testFileList = []
evalFileList = []
for file in os.listdir():
    if file.endswith(""):
        filePath = f"{packetTestFolder}\{file}"
        testFileList.append(filePath)
    if file.endswith(".a"):
        filePath = f"{packetTestFolder}\{file}"
        evalFileList.append(filePath)

def processTestFile(filePath):
    #*return the list of results
    #open file
    myFileT = open(filePath, "r")
    myLineT = myFileT.readline()
    #read header
    header = myLineT
    #create instance of buffer
    buffer_size, n_requests = map(int, header.split())
    requests = []
    #for each data row call the method the request method
    myLineT = myFileT.readline()
    while myLineT:
        arrived_at, time_to_process = map(int, myLineT.split())
        requests.append(arrived_at, time_to_process)
        myLineT = myFileT.readline()

    buffer = packets.Buffer(buffer_size)
    for request in requests:
        packets.Buffer.process(buffer, request)
    #append the result to the list
    returnList = []
    for each in buffer.finish_time:
        returnList.append(each)
    #return list
    return returnList

def processEvalFile(filePath):
    myFileE = open(filePath, "r")
    myLineE = myFileE.readline()
    returnList = []
    while myLineE:
        returnList.append(myLineE)
        myLineE = myFileE.readline()
    return returnList
class TestPackets(unittest.TestCase):
    def test(self):
        for i in range(len(testFileList)):            
            testExample = processTestFile(testFileList[i])
            evalExample = processEvalFile(evalFileList[i])
        
            for j in range(len(testExample)):
                self.assertEqual(testExample[j], evalExample[j])
    
    
if __name__ == '__main__':
    unittest.main()    
