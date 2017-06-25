from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.aggregates import Count
from .models import Union,Member
from .forms import UnionForm, MemberForm, RegisterForm
from haystack.forms import SearchForm

IMAGE_FILE_TYPE = ['jpg', 'png', 'jpeg']

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:	
		unions = Union.objects.filter(user=request.user).annotate(num_people=Count('member'))
		return render(request, 'union/index.html', {'unions':unions})

def detail(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		union = get_object_or_404(Union, pk=union_id)
		return render(request, 'union/detail.html', {'union': union})

def union_info(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		union = get_object_or_404(Union, pk=union_id)
		return render(request, 'union/union_info.html', {'union': union})

def union_add(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		form = UnionForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			union = form.save(commit=False)
			union.user = request.user
			union.logo = request.FILES['logo']
			union.save()

			file_type = union.logo.url.split('.')[-1].lower()

			if file_type not in IMAGE_FILE_TYPE:
				context = {
					'form': form,
					'error_message': 'Image file must be PNG, JPG, or JPEG'
				}
				return render(request, 'union/union_add.html', context)
			else:
				return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union.id}))

		return render(request, 'union/union_add.html', {'form': form})


def union_edit(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		union = get_object_or_404(Union, pk=union_id)
		if request.method == 'POST':
			form = UnionForm(request.POST or None, request.FILES or None, instance=union)
			if form.is_valid:
				union_info = form.save(commit=False)
				union_info.user = request.user
				union_info.save()
				return HttpResponseRedirect(reverse('union:index'))

		if request.method == 'GET':
			form = UnionForm(instance=union)
		return render(request, 'union/union_edit.html', {'form': form})
		
def union_delete(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		union = get_object_or_404(Union, pk=union_id)
		union.delete()
		return HttpResponseRedirect(reverse('union:index'))


def member_add(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		form = MemberForm(request.POST or None)
		union = get_object_or_404(Union, pk=union_id)

		if form.is_valid():
			member = form.save(commit=False)
			member.union = union
			member.save()

			return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union_id}))

		context = {
			'form': form,
			'union': union,
		}
		return render(request, 'union/member_add.html', context)

def member_delete(request, member_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		member = get_object_or_404(Member, pk=member_id)
		union_id = member.union.id
		member.delete()

		return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union_id}))

def member_edit(request, member_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		member = get_object_or_404(Member, pk=member_id)
		union = member.union
		if request.method == "POST":
			form = MemberForm(request.POST or None, instance=member)
			if form.is_valid():
				member_info = form.save(commit=False)
				member_info.union = union
				member_info.save()
				return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union.id}))
	
		if request.method == "GET":
			form = MemberForm(instance=member) #store the original info
		context = {
			'form':form,
			'union':union
		}
		return render(request, 'union/member_edit.html', context)


def view_all(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	else:
		unions = Union.objects.filter(user=request.user)
		members = []

		for union in unions:
			members += union.member_set.all()
		return render(request, 'union/view_all.html', {'members':members})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegisterForm()

	return render(request, 'union/register.html', {'form':form})


def full_search(request):
	sform = SearchForm(request.GET)
	members = sform.search()
	return render(request, 'union/full_search.html', {'members': members})
