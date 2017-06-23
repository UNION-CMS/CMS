from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Union, Member, User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class RegisterForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email')

class UnionForm(forms.ModelForm):

	class Meta:
		model = Union
		fields = ['name', 'logo', 'info']


class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ['name', 'member_id', 'major','sex', 'position']