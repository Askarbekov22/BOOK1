from django.urls import path
from . import views
from . import models

apps_name = 'product'
urlpatterns = [
    path('product/', views.ProductListView.as_view(queryset=models.ProductCL.objects.all()),
         name='product'),
    path('product/dior', views.ProductListView.as_view(queryset=models.ProductCL.objects.filter(tag__name='Nike')),
         name='Nike'),
    path('product/gucci', views.ProductListView.as_view(queryset=models.ProductCL.objects.filter(tag__name='Adidas')),
         name='Adidas'),
    path('product/chanel', views.ProductListView.as_view(queryset=models.ProductCL.objects.filter(tag__name='Gucci')),
         name='Gucci'),
    path('product/celvincline',
         views.ProductListView.as_view(queryset=models.ProductCL.objects.filter(tag__name='Naruto')),
         name='Naruto'),
    path('create/', views.OrderCreateView.as_view(), name='create')
]
