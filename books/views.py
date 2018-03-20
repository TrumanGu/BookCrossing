from django.shortcuts import render,redirect,Http404
from django.views import View
from books.models import *
from .forms import RegisterForm
from django.db.models import Q


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def BookList(request):
    book_list = Goods.objects.all()
    book_type_list = Category.objects.all()
    paginator = Paginator(book_list, 9)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        print(page)
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    return render(request, 'books/books.html', locals())







def BookDetail(request,nid):
    try:
        book_obj = Goods.objects.get(pk=nid)
        return render(request, 'books/detail.html',{'book_obj':book_obj})
    except Exception:
        raise Http404




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'books/register.html', {'form':form})


def search(request):
    q = request.GET.get('q')
    err_message = ''
    if not q:
        err_message =  '请输入关键词'
        return render(request, 'books/books.html', locals())
    book_list = Goods.objects.filter(Q(good_name__icontains=q)| Q(good_category__caption__icontains=q)|Q(good_context__icontains=q))
    return render(request, 'books/books.html',locals())