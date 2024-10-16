from django.shortcuts import render

# index.html のview関数
def index(request):
    params = {
        'title':'Taishiのホームページ',
        'logo_url':'index',
        'intro_url':'intro',
    }
    return render(request, 'pages/index.html', params)


# introduction.html のview関数
def introduction(request):
    params = {
        'logo_url':'index',
    }
    return render(request, 'pages/introduction.html', params)