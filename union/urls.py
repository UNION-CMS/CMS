from django.conf.urls import url,include
from . import views

app_name = 'union'

urlpatterns = [
	#
    url(r'^$', views.index, name='index'),

    #/<union_id>/detail
    url(r'^(?P<union_id>[0-9]+)/detail/$', views.detail, name='detail'),

    #/<union_id>/detail
    url(r'^(?P<union_id>[0-9]+)/union_info/$', views.union_info, name='union_info'),

    #/union_add/
    url(r'^union_add/$', views.union_add, name='union_add'),
    
    #/<union_id>/union_edit
    url(r'^(?P<union_id>[0-9]+)/union_edit/$', views.union_edit, name='union_edit'),
    
    #/<union_id>/union_delete
    url(r'^(?P<union_id>[0-9]+)/union_delete/$', views.union_delete, name='union_delete'),

    #/view_all
    url(r'^view_all/$', views.view_all, name='view_all'),
    
    #/users/register
    url(r'^users/register/$', views.register, name='register'),


    #/<union_id>/member_add
    url(r'^(?P<union_id>[0-9]+)/member_add/$', views.member_add, name='member_add'),

    #/<member_id>/member_delete
    url(r'^(?P<member_id>[0-9]+)/member_delete/$', views.member_delete, name='member_delete'),

    #/<member_id>/member_edit
    url(r'^(?P<member_id>[0-9]+)/member_edit/$', views.member_edit, name='member_edit'),
]
