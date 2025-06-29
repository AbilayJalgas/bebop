from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('news/<int:pk>', views.news_page),
    path('search', views.search),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
]
