from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Game, Review, Collection
from .models import *
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login

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

# creating profile view
class CreateProfileView(CreateView):
    '''The view to create a single profile'''
    model = Profile
    form_class = UserRegistrationForm
    template_name = "project/create_profile_form.html"

    def get_context_data(self, **kwargs):
        # Call superclass method for context
        context = super().get_context_data(**kwargs)
        # Add instance of UserCreationForm
        context['user_create'] = UserCreationForm()
        return context

    def form_valid(self, form):
        # Remake UserCreationForm from POST data
        user_form = UserCreationForm(self.request.POST)
        # If valid
        if user_form.is_valid():
            # Save user and add to profile
            user = user_form.save()
            form.instance.user = user
            # Log user in automatically if successful
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Render the form with errors
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class ShowProfilePageView(DetailView):
    '''the view to show a single profile'''
    model = Profile
    template_name = "project/show_profile.html"
    context_object_name = "profile"