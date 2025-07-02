from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('news/<int:pk>', views.news_page),
    path('search', views.search),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('to-favourites/<int:pk>', views.add_to_favourites),
    path('del-from-favourites/<int:pk>', views.del_from_favourites),
    path('favourites', views.show_favourites)
]
