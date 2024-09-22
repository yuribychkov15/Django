from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# Create your views here.

# create two lists, one for quotes and one for images

quotes = [
    "Talent wihtout working hard is nothing.",
    "Winning - that's the most important to me. It's as simple as that.",
    "There are people out there who hate me and who say I'm arrogant, vain, and whatever. That's all part of my success. I am made to be the best.",
    "I don't mind people hating me, because it pushes me.",
    "I see myself as the best footballer in the world. If you don't believe you are the best, then you will never achieve all that you are capable of.",
]

images = [
    "quotes/images/ronaldo1.jpeg",
    "quotes/images/ronaldo2.jpeg",
    "quotes/images/ronaldo3.jpg",
    "quotes/images/ronaldo4.jpeg",
    "quotes/images/ronaldo5.jpeg",
]


def quote(request):
    '''
    Function to handle the URL request for /quotes/quote (quote page).
    Delegate rendering to the template quotes/quote.html.
    '''
    template_name = "quotes/quote.html"
    # select a random quote and image
    quote_selected = random.choice(quotes)
    image_selected = random.choice(images)
    # a dictionary of variables for the template including the quote, image, and current time
    context = {
        "quote_selected" : quote_selected,
        "image_selected" : image_selected,
        "current_time" : time.ctime(),
    }
    return render(request, template_name, context)


def show_all(request):
    '''
    Function to handle the URL request for /quotes/show_all (show all quotes page).
    Delegate rendering to the template quotes/show_all.html.
    '''
    template_name = "quotes/show_all.html"
    # a dictionary of variables for the template including the quotes, images, and current time
    context = {
        "quotes" : quotes,
        "images" : images,
        "current_time" : time.ctime(),
    }
    return render(request, template_name, context)

def about(request):
    '''
    Function to handle the URL request for /quotes/about (about page).
    Delegate rendering to the template quotes/about.html.
    '''
    # use this template to render the response
    template_name = 'quotes/about.html'

    # create a dictionary of context variables for the template:
    context = {
        "current_time" : time.ctime(),
    }

    # delegate rendering work to the template
    return render(request, template_name, context)