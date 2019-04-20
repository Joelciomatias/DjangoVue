from django.urls import path
from . import views

urlpatterns = [
    path('/topics/<region_id>/', views.topics),
    path('/search/<query>/', views.search),
]
