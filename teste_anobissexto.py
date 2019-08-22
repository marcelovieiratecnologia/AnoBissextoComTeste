from app import anoBissexto
from unittest import TestCase

class testeBissexto(TestCase):
		
		def testeBissexto_EhNumerico(self):
				try:
						anoBissexto(1)
						pass
				except:
						self.fail("Falha Inesperada.")
		
		def testeBissexto_MenorIgualZero(self):
				with self.assertRaises(ValueError):
						anoBissexto(0)

		def testeBissexto_NaoEhNumerico(self):
				with self.assertRaises(TypeError):
						anoBissexto("asdasd")

		def testesAnosBisextos(self):
				vrsEntradas = [1600,1732,1888,1944,2008]
				vrEsperado = True
				for vr in vrsEntradas:
						with self.subTest(vr=vr):
								self.assertEqual(anoBissexto(vr), vrEsperado)

		def testesAnoNaoBissextos(self):
				vrsEntradas = [1742,1889,1951,2011]
				vrEsperado = False
				for vr in vrsEntradas:
						with self.subTest(vr=vr):
								self.assertEqual(anoBissexto(vr), vrEsperado)


if __name__ == '__main__':
    TestCase.main()