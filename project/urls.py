## project/urls.py
## description: URL patterns for the project app

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import auth views

urlpatterns = [
    # show profile
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    path('profile/<int:pk>/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    # game urls
    path('', views.GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('game/add/', views.GameCreateView.as_view(), name='game_add'),
    # review urls
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/add/', views.ReviewCreateView.as_view(), name='review_add'),
    path('game/<int:game_id>/reviews/add/', views.ReviewCreateView.as_view(), name='review_add'),
    path('reviews/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
    # collections url
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('game/<int:game_id>/add_to_collection/', views.AddToCollectionView.as_view(), name='add_to_collection'),
    path('collection/<int:pk>/delete/', views.DeleteCollectionView.as_view(), name='delete_collection'),
    # authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='project/logged_out.html'), name='logout'),
    # users
    path('users/add/', views.CreateProfileView.as_view(), name='user_add'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]

