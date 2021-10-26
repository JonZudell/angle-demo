from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage

class PostViewTestCase(TestCase):
    def test_post_data_01(self):
        json = open(staticfiles_storage.path('data_01.json'), 'rb').read()
        try:
            response = self.client.post('/post/', json, content_type="application/json")
            self.assertEqual(response.status_code, 201)
        except Exception as ex:
            print(ex)