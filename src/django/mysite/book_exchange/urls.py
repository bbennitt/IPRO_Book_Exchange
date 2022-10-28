from django.contrib import admin
from django.urls import path, include


from . import views
#from django.mysite import book_exchange

app_name = 'book_exchange'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('api/', views.ApiOverview, name='api-home'),
    path('api/create/', views.ApiOverview, name='add-school'),
    path('<int:pk>/', views.MainView.as_view(), name='main'),
    path('<int:pk>/buy/', views.BuyView.as_view(), name='buy'),
    path('<int:pk>/sell/', views.SellView.as_view(), name='sell'),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name='profile'),
    path('<user_id>/buy/<book_for_sale_id>/', views.book_info, name='book_info'),
    #path('api/', include(book_exchange.urls)),

    #path('<user_id>/buy/<book_id>', , name='sell'),
    #path('<user_id>/sell/', views.SellView.as_view(), name='sell'),
]