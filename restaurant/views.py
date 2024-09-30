from django.shortcuts import render
from django.utils import timezone
import random
import time

def main(request):
    '''
    Function to handle the URL request for /restaurant/main.
    This will be going to the template restaurant/main.html.
    '''
    template_name = 'restaurant/main.html'
    # context variable to send
    context = {
        "current_time" : timezone.now(),
    }
    return render(request, template_name, context)

def order(request):
    '''
    Function to handle the URL request for /restaurant/order.
    This will be going to the template restaurant/order.html.
    '''
    template_name = 'restaurant/order.html'

    # make up a list of four daily specials to choose from
    daily_specials = ["Kofta Kebab Over Rice", "Fish Over Rice", "Lamb Over Rice"]
    # randomly choose our daily special
    daily_special = random.choice(daily_specials)
    # randomly choose a price for the daily special
    daily_special_price = random.randint(10, 20)
    # context variables to send 
    context = {
        'daily_special': daily_special,
        'daily_special_price': daily_special_price,
        "current_time" : timezone.now(),
    }
    return render(request, template_name, context)

def confirmation(request):
    '''
    Function to handle the URL request for /restaurant/confirmation.
    This will be going to the template restaurant/confirmation.html.
    '''
    template_name = 'restaurant/confirmation.html'

    if request.method == 'POST':
        # get the items ordered
        items_ordered = request.POST.getlist('items')
        # get the customer's name, phone, email, and special instructions
        customer_name = request.POST.get('name')
        customer_phone = request.POST.get('phone')
        customer_email = request.POST.get('email')
        special_instructions = request.POST.get('instructions')

        # calculate the total price
        total_price = 0
        for item in items_ordered:
            price = request.POST.get(f'{item}_price')
            if price is not None:
                total_price += float(price)

        # https://docs.python.org/3/library/datetime.html
        # randomly choose between 30-60 minutes for the ready time
        ready_time = timezone.now() + timezone.timedelta(minutes=random.randint(30, 60))

        # context variables to send
        context = {
            'items_ordered': items_ordered,
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'customer_email': customer_email,
            'special_instructions': special_instructions,
            'total_price': total_price,
            'ready_time': ready_time,
            "current_time" : timezone.now(),
        }
        return render(request, template_name, context)
    # if no post, just rerender back to the starting order page
    return render(request, 'restaurant/order.html')