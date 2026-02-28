from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages # Required for Delete success messages
from .models import Product

# 1. READ (The Dashboard)
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    # Feature: Order products so newest appearing first
    ordering = ['-id'] 

# 2. CREATE (The "Add" Feature)
class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = ['sku', 'name', 'category', 'quantity', 'price']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product '%(name)s' was created successfully!"

# 3. UPDATE (The "Edit" Feature)
class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['sku', 'name', 'category', 'quantity', 'price']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product '%(name)s' was updated successfully!"

# 4. DELETE (The "Fix/Module" Feature)
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    # DeleteView doesn't support SuccessMessageMixin easily, so we use this:
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Product deleted successfully!")
        return super().delete(request, *args, **kwargs)