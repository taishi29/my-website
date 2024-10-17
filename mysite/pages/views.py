from django.shortcuts import render
from .forms import ContactForm
# index.html のview関数
def index(request):
    params = {
        'title':'Taishiのホームページ',     
    }
    return render(request, 'pages/index.html', params)


# introduction.html のview関数
def introduction(request):
    params = {
    }
    return render(request, 'pages/introduction.html', params)


# contact.html のviwe関数
def contact(request):
    params = {
        'form':ContactForm(),
    }
    return render(request, 'pages/contact.html', params)