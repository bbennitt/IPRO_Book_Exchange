from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Book

# each view is a different "template" for what we display on the webpage
# for example, main page, sell page, buy page, info page, etc.
# we are going to have 
# 1. login page (I think this is seperate)
# 2. main page
# 3. buy page
# 4. sell page
# 5. profile page


#class SellView(generic.DetailView):
 #   template_name = 'polls/results.html'

def login(request):
    books_list = Book.objects.order_by('ISBN')
    output = ", ".join([b.title for b in books_list])
    return HttpResponse('The books currently in the database are: %s' % output)

def main(request, user_id):
    return HttpResponse("You're looking at the main page for user %s." % user_id)

def buy(request, user_id):
    return HttpResponse("You're looking at the buy page for user %s." % user_id)

def sell(request, user_id):
    return HttpResponse("You're looking at the sell page for user %s." % user_id)

def profile(request, user_id):
    return HttpResponse("You're looking at the profile page for user %s." % user_id)


