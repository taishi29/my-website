from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls') ), # include関数は、引数に指定したモジュールを呼び出す。'pages'フォルダ内のurls.pyが読み込まれ、pages/より後のアドレスがそこから割り当てられる。
]
