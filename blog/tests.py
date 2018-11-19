from django.test import TestCase, Client


class BlogTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_access_success(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code, 'status code == 200')

    def test_index_access_failed(self):
        response = self.client.get('/test')
        self.assertEqual(404, response.status_code, 'status code == 404')
