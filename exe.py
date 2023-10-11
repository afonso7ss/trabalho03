import unittest

def inverter(texto):
    nome=''
    for letra in range(len(texto)-1,-1,-1):
        nome +=texto[letra]
    return nome

class TestInverterString(unittest.TestCase):

    def test_inverter_string(self):
        resultado = inverter("Hello, World!")
        self.assertEqual(resultado, "!dlroW ,olleH")

if __name__ == '__main__':
    unittest.main()





