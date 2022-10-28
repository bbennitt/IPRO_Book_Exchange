from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .serializers import ItemSerializer

from .models import Book, BookForSale, School, User


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

class LoginView(generic.ListView):
    model = User
    template_name = 'book_exchange/signin.html'

    #books_list = Book.objects.order_by('ISBN')
    #output = ", ".join([b.title for b in books_list])
    #return HttpResponse('The books currently in the database are: %s' % output)

class MainView(generic.DetailView):
    model = User
    template_name = 'book_exchange/mainpage.html'

class BuyView(generic.DetailView):
    model = User
    template_name = 'book_exchange/User_Buy_Page.html'

class SellView(generic.DetailView):
    model = User
    template_name = 'book_exchange/User_Sell_Forum.html'

class ProfileView(generic.DetailView):
    model = User
    template_name = 'book_exchange/profile.html'

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

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by School Name': '/?school_name=category_name',
        'Search by City': '/?city=category_name',
        'Search by State': '/?state=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)

@api_view(['POST'])
def add_school(request):
    school = ItemSerializer(data=request.data)

    #validate for existing data
    if School.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data is already exists')

    if school.is_valid():
        school.save()
        return Response(school.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)