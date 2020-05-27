from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from . import apiviews

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Create your tests here.

# factory = APIRequestFactory()
# request =  factory.post(uri)

# class TestPoll(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = apiviews.PollViewSet.as_view({'get':'list'})
#         self.uri = '/polls/'

#         def test_list(self):
#             request = self.factory.get(self.uri)
#             response = self.views(request)
#             self.assertEqual(response.status_code, 200, 'Expected Responce Code recived {0} instead.'.format(response.status_code))

class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.views = apiviews.PollViewSet.as_view({'get':'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user = self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user('jtest',email='jangotest002@gmail.com', password='das312das312')

    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.views(request)
        
# class TestPoll(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.factory = APIRequestFactory()
#         self.view = apiviews.PollViewSet.as_view({'get':'list'})
#         self.uri = '/polls/'

    def test_list2(self):
        self.client.login(username='jtest',password='das312das312')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))
