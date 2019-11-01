from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.booklist, name='books'),
	url(r'^authors/$', views.authorlist, name='authors'),
	url(r'^book/(?P<id>\d+)$', views.bookdetailview, name='book-detail'),
	url(r'^author/(?P<id>\d+)$', views.authordetailview, name='author-detail'),

]