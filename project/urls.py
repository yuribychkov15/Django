## project/urls.py
## description: URL patterns for the project app

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import auth views

urlpatterns = [
    # show profile
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    # game urls
    path('', views.GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    # review urls
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    # collections url
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),

        # authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='project/logged_out.html'), name='logout'),
]