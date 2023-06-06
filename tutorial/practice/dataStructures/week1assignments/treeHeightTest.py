import os

treeHeightTestFolder = r"C:\Users\achyu\OneDrive\Desktop\week1_basic_data_structures\2_tree_height\tests"
os.chdir(treeHeightTestFolder)

def load(filePath):
        with open(filePath, 'r') as f:
            return f.read()
        
testList = []
evalList = []
for file in os.listdir():
    if file.endswith(".a"):
        filePath = f"{treeHeightTestFolder}\{file}"
        evalList.append(filePath)
    else:
        filePath = f"{treeHeightTestFolder}\{file}"
        testList.append(filePath)
        
