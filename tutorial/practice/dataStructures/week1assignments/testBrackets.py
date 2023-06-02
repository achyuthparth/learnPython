import unittest
import packets
import os




class TestBrackets(unittest.TestCase):
    def testBrackets(self):
        readFileList = [
            'File'
            for _ in os.listdir(
                'C:/Users/achyu/AppData/Local/Temp/MicrosoftEdgeDownloads/a66ad46f-c584-4498-a947-0362da97e042/aEZeXmftT0CGXl5n7T9A4g_a3dedcb00f6b4586b61ae7a92ff30779_course2_2003291203.zip/week1_basic_data_structures/1_brackets_in_code/tests'
            )
            if os.path.isfile('File')
        ]
        checkFileList = [
            'A File'
            for _ in os.listdir(
                'C:/Users/achyu/AppData/Local/Temp/MicrosoftEdgeDownloads/a66ad46f-c584-4498-a947-0362da97e042/aEZeXmftT0CGXl5n7T9A4g_a3dedcb00f6b4586b61ae7a92ff30779_course2_2003291203.zip/week1_basic_data_structures/1_brackets_in_code/tests'
            )
            if os.path.isfile('A File')
        ]
        