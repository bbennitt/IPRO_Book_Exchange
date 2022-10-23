from django.urls import path

from . import views

app_name = 'book_exchange'
urlpatterns = [
    path('', views.login, name='login'),
    path('<user_id>/', views.main, name='main'),
    path('<user_id>/buy/', views.buy, name='buy'),
    path('<user_id>/sell/', views.sell, name='sell'),
    path('<user_id>/profile/', views.profile, name='profile'),
    #path('<user_id>/buy/<book_id>', , name='sell'),
    #path('<user_id>/sell/', views.SellView.as_view(), name='sell'),
]