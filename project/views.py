from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Game, Review, Collection

# Create your views here.

class GameListView(ListView):
    ''' Our games to be listed '''
    model = Game
    template_name = 'project/game_list.html'  
    context_object_name = 'games'

class GameDetailView(DetailView):
    ''' Our individual game details '''
    model = Game
    template_name = 'project/game_detail.html'

class ReviewListView(ListView):
    ''' Our reviews to be listed '''
    model = Review
    template_name = 'project/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    ''' User individual review for a game '''
    model = Review
    template_name = 'project/review_detail.html'

# Collection Views
class CollectionListView(ListView):
    ''' Show all of a user's collection '''
    model = Collection
    template_name = 'project/collection_list.html'
    context_object_name = 'collections'
