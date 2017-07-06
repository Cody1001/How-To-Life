from django.conf.urls import url
from . import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.home, name='home'),
#    url(r'^play/$', views.play, name='play'),
#    url(r'^results/$', views.results, name='results'),
]
