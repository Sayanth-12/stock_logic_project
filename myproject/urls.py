# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from inventory import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductListView.as_view(), name='product_list'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    
    # ADD THESE TWO LINES BELOW:
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]