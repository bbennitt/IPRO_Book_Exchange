from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from . import views


app_name = 'book_exchange'

router = routers.DefaultRouter()
router.register(r'school', views.SchoolViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'pinned_book', views.PinnedBookViewSet)
router.register(r'transaction', views.TransactionViewSet)


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<int:pk>/', views.MainView.as_view(), name='main'),
    path('<int:pk>/buy/', views.browse_books, name='browse_books'),
    path('<user_id>/sell/', views.sell_view, name='sell_view'),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name='profile'),
    path('<user_id>/buy/<book_for_sale_id>/', views.book_info, name='book_info'),

    #path('<user_id>/buy/<book_id>', , name='sell'),
    #path('<int:pk>/sell/', views.SellView.as_view(), name='sell'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)