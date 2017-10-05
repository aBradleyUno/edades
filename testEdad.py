import unittest
from Edad import Edad

class TestFiguras(unittest.TestCase):
    def setUp(self):
        self.edad = Edad()
    def test_not_valid(self):
        self.edad.calculate_edad('c')
        self.assertEquals(self.edad.getResultado(), "no valido")
    def test_non_existent(self):
        self.edad.calculate_edad(-2)
        self.assertEquals(self.edad.getResultado(), "no existes")
    def test_minor(self):
        self.edad.calculate_edad(10)
        self.assertEquals(self.edad.getResultado(), "eres nino")
    def test_adolecent(self):
        self.edad.calculate_edad(16)
        self.assertEquals(self.edad.getResultado(), "eres adolecente")
    def test_adult(self):
        self.edad.calculate_edad(26)
        self.assertEquals(self.edad.getResultado(), "eres adulto")
    def test_adult_old(self):
        self.edad.calculate_edad(100)
        self.assertEquals(self.edad.getResultado(), "eres adulto mayor")
    def test_mmm_ra(self):
        self.edad.calculate_edad(700)
        self.assertEquals(self.edad.getResultado(), "eres mumm-ra")
if __name__ == '__main__':
	unittest.main()
