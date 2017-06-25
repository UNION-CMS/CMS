from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from .models import User, Union
from .views import index

class SimpleTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='nothing', password='admin123')
		self.union = Union.objects.create()

	def test_login_index(self):
		request = self.factory.get('/')
		request.user = self.user
		response = index(request)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_index(self):
		request = self.factory.get('/')
		request.user = AnonymousUser()
		response = index(request)
		self.assertEqual(response.status_code, 302)

