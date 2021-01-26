from tir import Webapp
import unittest

class GFEC020(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC020")

    def test_GFEC020_CT001(self):

        self.oHelper.SearchBrowse("1200401")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("GU7_NRCID", "1200401")
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()