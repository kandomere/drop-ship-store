from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from shop.models import Product, AboutUsPhoto


class ProductsListViewHomeFour(ListView):
    model = Product
    template_name = 'index.html'
    ordering = ['-pk']


class AboutUsImages(ListView):
    model = AboutUsPhoto
    template_name = 'about-us.html'




def contact(request):
    return render(request, 'contact.html')

