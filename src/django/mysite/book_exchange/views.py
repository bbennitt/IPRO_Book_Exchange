from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Book, BookForSale, User

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
    #books_list = Book.objects.order_by('ISBN')
    #output = ", ".join([b.title for b in books_list])
    #return HttpResponse('The books currently in the database are: %s' % output)
    return render(request, 'book_exchange/signin.html')

def main(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'book_exchange/mainpage.html', {'user': user})
    #return HttpResponse("You're looking at the main page for user %s." % user_id)

def buy(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'book_exchange/User_Buy_Page.html', {'user': user})
    #return HttpResponse("You're looking at the buy page for user %s." % user_id)

def sell(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'book_exchange/User_Sell_Forum.html', {'user': user})
    #return HttpResponse("You're looking at the sell page for user %s." % user_id)

def profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'book_exchange/profile.html', {'user': user})
    #return HttpResponse("You're looking at the profile page for user %s." % user_id)

def book_info(request, user_id, book_for_sale_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    try:
        book = BookForSale.objects.get(pk=book_for_sale_id)
    except BookForSale.DoesNotExist:
        raise Http404("Book for sale does not exist")

    return render(request, 'book_exchange/Book_ID.html', {'user': user, 'book': book})

