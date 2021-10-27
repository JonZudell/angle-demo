
from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage
import json

def load_posts(name):
    return json.loads(open(staticfiles_storage.path(name), 'r').read())["posts"]

def post_data(client, json):
    return client.post('/post/', json, content_type="application/json")

def get_data(client, params=None):
    return json.loads(client.get('/post/', params).content)["posts"]

def unique_from_data(first, second):
    summed = list({ post['name'] : post for post in first}.values())
    return list({ post['name'] : post for post in second}.values()) + summed

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

    def test_post_filter(self):
        response = post_data(self.client, json.dumps({"posts" : self.valid_posts}))
        everything = get_data(self.client)
        above_1000 = get_data(self.client, {"min_price" : 1000})
        below_1000 = get_data(self.client, {"max_price" : 1000})

        summed = unique_from_data(above_1000, below_1000)
        self.assertEqual(len(everything), len(summed))

        
        between_0_500 = get_data(self.client, {"min_price" : 0, "max_price" : 500})
        between_500_1000 = get_data(self.client, {"min_price" : 500, "max_price" : 1000})
        summed = unique_from_data(between_0_500, between_500_1000)
        self.assertEqual(len(below_1000), len(summed))

        bad = get_data(self.client, {"keyword" : "newpost"})

        self.assertEqual(len(bad), 0)
        response = post_data(self.client, json.dumps({"posts" : [{"name" : "newpost", "start_date" : "04/04/2022", "price" : 0}]}))
        good = json.loads(response.content)
        self.assertEqual(len(good), 1)

        search = get_data(self.client, {"keyword" : "newpost"})
        self.assertEqual(len(search), 1)