
from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage
import json

def load_posts(name):
    return json.loads(open(staticfiles_storage.path(name), 'r').read())["posts"]

def post_data(client, json):
    return client.post('/post/', json, content_type="application/json")

class PostViewTestCase(TestCase):
    def setUp(self):
        self.all_posts = load_posts('data_01.json')
        self.all_posts.extend(load_posts('data_02.json'))
        self.all_posts.extend(load_posts('data_03.json'))

        response = post_data(self.client, json.dumps({"posts" : self.all_posts}))
        self.assertEqual(response.status_code, 400)

        self.post_errors = json.loads(response.content)["posts"]
        
        self.valid_posts = []
        self.invalid_posts = []

        for error, post in zip(self.post_errors, self.all_posts):
            if not error:
                self.valid_posts.append(post)
            else:
                self.invalid_posts.append(post)

    def test_post_data(self):
        response = post_data(self.client, json.dumps({"posts" : self.valid_posts}))
        self.assertEqual(response.status_code, 201)
    
    def test_post_sums(self):
        self.assertEqual(len(self.all_posts), len(self.valid_posts) + len(self.invalid_posts))