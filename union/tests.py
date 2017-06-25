from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from .models import User, Union
from .views import index, detail, union_info, union_add, union_edit, union_delete, member_add, member_edit, member_delete

class SimpleTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='nothing', password='admin123')
		self.union = Union.objects.create(name='newUnion', logo='https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3058540266,4055511415&fm=26&gp=0.jpg', info='nothing')
		self.union.user = self.user

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

	def test_login_detail(self):
		request = self.factory.get('/1/detail/')
		request.user = self.user
		response = detail(request, 1)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_detail(self):
		request = self.factory.get('/1/detail/')
		request.user = AnonymousUser()
		response = detail(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_login_union_info(self):
		request = self.factory.get('/1/union_info/')
		request.user = self.user
		response = union_info(request, 1)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_union_info(self):
		request = self.factory.get('/1/union_info/')
		request.user = AnonymousUser()
		response = union_info(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_login_union_add(self):
		request = self.factory.get('/union_add/')
		request.user = self.user
		response = union_add(request)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_union_add(self):
		request = self.factory.get('/union_add/')
		request.user = AnonymousUser()
		response = union_add(request)
		self.assertEqual(response.status_code, 302)

	def test_login_union_edit(self):
		request = self.factory.get('/1/union_edit/')
		request.user = self.user
		response = union_edit(request, 1)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_union_edit(self):
		request = self.factory.get('/1/union_edit/')
		request.user = AnonymousUser()
		response = union_edit(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_login_union_delete(self):
		request = self.factory.get('/1/union_delete/')
		request.user = self.user
		response = union_delete(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_Anonymouse_union_delete(self):
		request = self.factory.get('/1/union_delete/')
		request.user = AnonymousUser()
		response = union_delete(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_login_member_add(self):
		request = self.factory.get('/1/member_add/')
		request.user = self.user
		response = member_add(request, 1)
		self.assertEqual(response.status_code, 200)

	def test_Anonymouse_member_add(self):
		request = self.factory.get('/1/member_add/')
		request.user = AnonymousUser()
		response = member_add(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_Anonymouse_member_edit(self):
		request = self.factory.get('/1/member_edit/')
		request.user = AnonymousUser()
		response = member_edit(request, 1)
		self.assertEqual(response.status_code, 302)

	def test_Anonymouse_member_delete(self):
		request = self.factory.get('/1/member_delete/')
		request.user = AnonymousUser()
		response = member_delete(request, 1)
		self.assertEqual(response.status_code, 302)