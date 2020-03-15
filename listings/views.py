from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'pages/listing.html')

def search(request):
    return render(request, 'pages/search.html')