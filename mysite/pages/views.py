from django.shortcuts import render

# index.html のview関数
def index(request):
    params = {
        'title':'Taishiのホームページ',
    }
    return render(request, 'pages/index.html', params)
