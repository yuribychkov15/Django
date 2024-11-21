## project/urls.py
## description: URL patterns for the project app

from django.urls import path
from .views import GameListView, GameDetailView, ReviewListView, ReviewDetailView, CollectionListView



urlpatterns = [
    # game urls
    path('', GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    # review urls
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    # collections url
    path('collections/', CollectionListView.as_view(), name='collection_list'),
]