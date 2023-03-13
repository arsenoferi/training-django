from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from . import models
# Create your views here.

def index(request):
    num_books = models.Book.objects.all().count()
    num_instance = models.BookInstance.objects.all().count()
    num_instance_aval = models.BookInstance.objects.filter(status__exact='a').count()

    context ={
        'num_books':num_books,
        'num_instance': num_instance,
        'num_instance_aval':num_instance_aval
    }

    return render(request,'catalog/index.html',context=context)

class BookCreate(CreateView):
    model = models.Book
    fields = '__all__'
    success_url = reverse_lazy('catalog:index')

class BookDetail(DetailView):
    model = models.Book
    
    
