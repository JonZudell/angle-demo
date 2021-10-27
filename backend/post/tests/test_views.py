
from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage
import json

class PostViewTestCase(TestCase):
    def test_post_data(self):
        results = []
        data = json.loads(open(staticfiles_storage.path('data_01.json'), 'r').read())
        results.extend(data["posts"])
        data = json.loads(open(staticfiles_storage.path('data_02.json'), 'r').read())
        results.extend(data["posts"])
        data = json.loads(open(staticfiles_storage.path('data_03.json'), 'r').read())
        results.extend(data["posts"])
        response = self.post_data(json.dumps({"posts" : results}))
        self.assertEqual(response.status_code, 400)

        errors = json.loads(response.content)["posts"]
        err_ndx = []
        # can do in one iteration
        for ndx, error in enumerate(errors):
            if error:
                err_ndx.append(ndx)

        for ndx in reversed(err_ndx):
            del results[ndx]

        response = self.post_data(json.dumps({"posts" : results}))
        self.assertEqual(response.status_code, 201)

    def post_data(self, json):
        return self.client.post('/post/', json, content_type="application/json")