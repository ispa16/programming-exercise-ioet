import unittest
import utils


class TestUtils(unittest.TestCase):

    
    def test_inputData(self):
        self.assertEqual(str(type(utils.inputData('data'))),'<class \'list\'>')
        self.assertEqual(str(type(utils.inputData('data2'))),'<class \'list\'>')
        self.assertEqual(str(type(utils.inputData('data3'))),'<class \'list\'>')
        self.assertEqual(str(type(utils.inputData('data4'))),'<class \'list\'>')
    def test_rangeTime(self):
        self.assertEqual(len(utils.rangeTime(10.00,11.00)),59)
        self.assertEqual(len(utils.rangeTime(00.00,14.00)),839)
        self.assertEqual(len(utils.rangeTime(8.00,9.00)),59)
        self.assertEqual(len(utils.rangeTime(0.00,24.00)),1439)
    def test_getWorkingRange(self):
        testList1=[['MO10:00', '12:00'], ['TU10:00', '12:00'], ['TH01:00', '03:00'], ['SA14:00', '18:00'], ['SU20:00', ' 21:00\n']]
        testList2=[['MO10:00', '12:00'], ['TH12:00', '14:00'], ['SU20:00', '21:00\n']]
        testList3=[['MO10:00', '12:00'], ['TH12:00', '14:00'], ['SU20:00', '21:00\n']]
        self.assertEqual(len(utils.getWorkingRange(testList1)),5)
        self.assertEqual(len(utils.getWorkingRange(testList2)),3)
        self.assertEqual(len(utils.getWorkingRange(testList3)),3)
    def test_compareLists(self):
        testList1=[['MO10:00', '12:00'], ['TU10:00', '12:00'], ['TH01:00', '03:00'], ['SA14:00', '18:00'], ['SU20:00', ' 21:00\n']]
        testList2=[['MO10:00', '12:00'], ['TH12:00', '14:00'], ['SU20:00', '21:00\n']]
        testList3=[['MO10:00', '12:00'], ['TH12:00', '14:00'], ['SU20:00', '21:00\n']]
        testList4=[['MO01:00', '05:00']]
        self.assertEqual(utils.compareLists(testList1,testList3),2)
        self.assertEqual(utils.compareLists(testList3,testList2),3)
        self.assertEqual(utils.compareLists(testList1,testList4),0)
    def test_employeeMatchFrecuency(self):
        self.assertEqual(utils.employeeMatchFrecuency('data'),'RENE-ASTRID: 2'
                                    +'\nRENE-ANDRES: 2\nASTRID-ANDRES: 3\n')
        self.assertEqual(utils.employeeMatchFrecuency('data2'),'RENE-ASTRID: 3\n')
        self.assertEqual(utils.employeeMatchFrecuency('data4'),'RENE-ASTRID: 2\nRENE-JUAN: 4\n'+
            'RENE-MOISES: 3\nRENE-PIERO: 0\nASTRID-JUAN: 2\nASTRID-MOISES: 1\nASTRID-PIERO: 0\n'+
            'JUAN-MOISES: 3\nJUAN-PIERO: 0\nMOISES-PIERO: 0\n')
        self.assertEqual(utils.employeeMatchFrecuency('data3'),
            'RENE-ASTRID: 3\nRENE-JUAN: 5\nRENE-MOISES: 3\nRENE-PIERO: 2\nRENE-JUANITO: 4\nRENE-ROBERTO: 1\nASTRID-JUAN: 3\n'+
            'ASTRID-MOISES: 1\nASTRID-PIERO: 0\nASTRID-JUANITO: 3\nASTRID-ROBERTO: 1\nJUAN-MOISES: 3\nJUAN-PIERO: 2\n'+
            'JUAN-JUANITO: 4\nJUAN-ROBERTO: 1\nMOISES-PIERO: 2\nMOISES-JUANITO: 2\nMOISES-ROBERTO: 0\nPIERO-JUANITO: 1\n'+
            'PIERO-ROBERTO: 1\nJUANITO-ROBERTO: 1\n')

if __name__ == '__main__':
    unittest.main()
