# mini_fb/views.py
# define the views for the mini_fb app
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import * # import all of the models
from .forms import *

# class-based view 
# inherits from ListView
class ShowAllProfileViews(ListView):
    '''the view to show all profiles'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"


class ShowProfilePageView(DetailView):
    '''the view to show a single profile'''
    model = Profile
    template_name = "mini_fb/show_profile.html"
    context_object_name = "profile"

class CreateProfileView(LoginRequiredMixin, CreateView):
    '''the view to create a single profile'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    '''the view to create a status message for a profile'''
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_object(self):
        # get the Profile object for the logged-in user
        return get_object_or_404(Profile, user=self.request.user)

    def get_context_data(self, **kwargs):
        # get context data from super class
        context = super().get_context_data(**kwargs)
        # find the Profile identified by the PK from the URL pattern
        profile = self.get_object()
        # add Profile referred to by the URL into this context
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        # set profile for status message
        form.instance.profile = self.get_object()
        # save status message to db 
        sm = form.save()
        # look at files from form
        files = self.request.FILES.getlist('files')
        # need image object
        for file in files:
            image = Image(image_file=file, status_message=sm)
            image.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    
# task 3
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''the view to update a single profile'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
    
    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    
# task 4
class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    ''' the view to delete a status message from a profile'''
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status_message'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

class UpdateStatusMessageView(UpdateView):
    ''' the view to update a status message for a profile'''
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'status_message'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    
class CreateFriendView(LoginRequiredMixin, View):
    ''' the view to add a friend to a proifle '''

    def get_object(self):
        # get the Profile object for the logged-in user
        return get_object_or_404(Profile, user=self.request.user)
    
    def dispatch(self, request, *args, **kwargs):
        # Use object manager to find the requisite Profile objects, and then call the Profile's add_friend
        # https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
        profile = self.get_object()
        other = get_object_or_404(Profile, pk=kwargs['other_pk'])
        profile.add_friend(other)
        return redirect('show_profile', pk=profile.pk)
    
class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
    ''' the view to show friend suggestions '''
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'

    def get_object(self):
        # get the Profile object for the logged-in user
        return get_object_or_404(Profile, user=self.request.user)

    def get_context_data(self, **kwargs):
        # need to add friend suggestions to context
        context = super().get_context_data(**kwargs)
        context['suggestions'] = self.object.get_friend_suggestions()
        return context
    
class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    ''' the view to show our news feed '''
    model = Profile
    template_name = 'mini_fb/news_feed.html'

    def get_object(self):
        # get the Profile object for the logged-in user
        return get_object_or_404(Profile, user=self.request.user)

    def get_context_data(self, **kwargs):
        # add news feed to context
        context = super().get_context_data(**kwargs)
        context['news_feed'] = self.object.get_news_feed()
        return context