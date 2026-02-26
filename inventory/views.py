from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Product

# 1. READ (List all items)
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

# 2. CREATE (Add new item)
class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = ['sku', 'name', 'category', 'quantity', 'price']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product '%(name)s' was created successfully!"

# 3. UPDATE (Edit existing item)
class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['sku', 'name', 'category', 'quantity', 'price']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product '%(name)s' was updated successfully!"

# 4. DELETE (Remove item)
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')