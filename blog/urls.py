from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.NewPostFormView.as_view(), name='post_new'),
]
