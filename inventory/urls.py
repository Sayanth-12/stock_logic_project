# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    
    # ADD (OR FIX) THESE TWO LINES:
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]