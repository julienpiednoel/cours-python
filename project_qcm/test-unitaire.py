import unittest
from reponse import Reponse


class TestReponse(unittest.TestCase):
    def test_reponse_creation(self):
        # Créez une instance de la classe Reponse
        reponse = Reponse("a) Option A", True)

        # Vérifiez si les attributs ont été initialisés correctement
        self.assertEqual(reponse.option, "a) Option A")
        self.assertEqual(reponse.answer, True)


if __name__ == "__main__":
    unittest.main()