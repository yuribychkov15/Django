from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View, UpdateView
from .models import Game, Review, Collection
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from .forms import *

# Create your views here.

# Users
class UserListView(ListView):
    ''' View to list all the registered users '''
    model = User
    template_name='project/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(project_profile__isnull=False)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(collection__isnull=False).distinct()
        return context

# creating profile view
class CreateProfileView(CreateView):
    '''The view to create a single profile'''
    model = Profile
    form_class = CreateProfileForm
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
        print("User form data:", self.request.POST)
        
        # If valid
        if user_form.is_valid():
            print("User form is valid.")
            # Save user and add to profile
            user = user_form.save()
            print("User created:", user)
            
            form.instance.user = user
            # Log user in automatically if successful
            login(self.request, user)
            print("User logged in:", user)
            
            return super().form_valid(form)
        else:
            print("User form errors:", user_form.errors)
            # render the form with errors
            return redirect(reverse('game_list'))

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class ShowProfilePageView(DetailView):
    '''the view to show a single profile'''
    model = Profile
    template_name = "project/show_profile.html"
    context_object_name = "profile"

class GameCreateView(CreateView, LoginRequiredMixin):
       model = Game
       form_class = GameForm
       template_name = 'project/game_form.html'

       def get_success_url(self):
           return reverse('game_list')
       
# collection adding and removing
class DeleteCollectionView(LoginRequiredMixin, DeleteView):
    '''The view to delete a game from the user's collection'''
    model = Collection
    template_name = 'project/delete_collection_confirm.html'
    context_object_name = 'collection'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.user.project_profile.pk})
    

class AddToCollectionView(LoginRequiredMixin, View):
    ''' The view to add a game to the user's collection '''

    def post(self, request, *args, **kwargs):
        game = get_object_or_404(Game, pk=kwargs['game_id'])
        Collection.objects.get_or_create(user=request.user, game=game)
        return redirect(reverse('show_profile', kwargs={'pk': request.user.project_profile.pk}))
    
class ReviewCreateView(CreateView):
    ''' Class for creating a review'''
    model = Review
    template_name = 'project/review_form.html'

    # get the form class
    def get_form_class(self):
        if 'game_id' in self.kwargs:
            return ReviewFormWithoutGame
        return ReviewForm

    # validate the form
    def form_valid(self, form):
        if 'game_id' in self.kwargs:
            form.instance.game = get_object_or_404(Game, pk=self.kwargs['game_id'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if 'game_id' in self.kwargs:
            return reverse('game_detail', kwargs={'pk': self.kwargs['game_id']})
        return reverse('review_list')

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    ''' Class for updating a review '''
    model = Review
    form_class = ReviewFormWithoutGame
    template_name = 'project/review_form.html'

    # get the queryset
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    ''' class for deleting a review '''
    model = Review
    template_name = 'project/review_confirm_delete.html'

    # get the queryset
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse('review_list')

class EditProfileView(LoginRequiredMixin, UpdateView):
    ''' class for editing a profile '''
    model = Profile
    form_class = EditProfileForm
    template_name = 'project/edit_profile_form.html'

    def get_object(self):
        return self.request.user.project_profile

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
