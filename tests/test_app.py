import unittest
from src.app import app

class TestSistema(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_adicionar_tarefa(self):
        response = self.app.post(
            '/adicionar',
            data={
                'titulo': 'Teste',
                'descricao': 'Descrição teste'
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()