from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def menupage(request):


    return render(request ,'Ecommerce/menu.html',{})