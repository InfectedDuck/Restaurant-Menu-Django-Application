from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def home(request):
    return render(request, 'home.html')

def menu(request):
    menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu.html', {'menu_items': menu_items})

def menu_item_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return render(request, 'menu_item_detail.html', {'item': item})

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')  # Add a booking page if needed
