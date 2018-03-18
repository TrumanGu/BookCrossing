from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView, DetailView
from books.models import *


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class BookList(ListView):
    model = Goods
    template_name = 'books/books.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Goods.objects.all()
        context['book_type_list'] = Category.objects.all()
        return context

def search(request):
    q = request.GET.get('q')
    book_list = Goods.objects.filter(good_name__icontains=q)
    return render(request, 'books/books.html', {'book_list':book_list})

class BookDetail(DetailView):
    model = Goods
    template_name = 'books/detail.html'
    context_object_name = 'book_detail'
    def get_context_data(self, **kwargs):
        contexts= super().get_context_data(**kwargs)
        return contexts
    #TODO:detail需要完善