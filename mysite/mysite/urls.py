from django.contrib import admin
from django.urls import path, include
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls') ), # include関数は、引数に指定したモジュールを呼び出す。'pages'フォルダ内のurls.pyが読み込まれ、pages/より後のアドレスがそこから割り当てられる。
    path('match/', include('match.urls') ),
    path('trash_notifier/', include('trash_notifier.urls') ),
    path('', views.index, name='home'),  # トップページにアクセスした際に pages.views.index を表示
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)