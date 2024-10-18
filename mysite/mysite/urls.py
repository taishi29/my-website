from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls') ), # include関数は、引数に指定したモジュールを呼び出す。'pages'フォルダ内のurls.pyが読み込まれ、pages/より後のアドレスがそこから割り当てられる。
    path('', views.index, name='home'),  # トップページにアクセスした際に pages.views.index を表示
]
