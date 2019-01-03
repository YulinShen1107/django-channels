# chat/urls.py
# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
]