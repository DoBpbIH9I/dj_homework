from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()
    context = {'phones': all_phones}

    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phone': phones}

    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phone': phones}

    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phone': phones}

    return render(request, template, context)


def show_product(request, slug):

    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phones': phone}
    return render(request, template, context)
