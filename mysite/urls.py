from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from polls import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^polls/',include('polls.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]