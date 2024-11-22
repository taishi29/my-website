import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

# プロジェクトのルートディレクトリを指定
BASE_DIR = Path(__file__).resolve().parent.parent

# .envファイルを読み込む
load_dotenv(BASE_DIR / '.env')

# .envファイルからSECRET_KEYを取得。取得できない場合は例外を発生させる。
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables")

# デバッグモードを環境変数から取得し、True/Falseに変換
DEBUG = False

# ホスト設定
ALLOWED_HOSTS = ['taishi-sushi.com', 'www.taishi-sushi.com', '13.211.242.180', '172.31.8.194', '127.0.0.1', 'localhost', '.pythonanywhere.com', 'taishi-sushi-elb-1983899373.ap-southeast-2.elb.amazonaws.com']

# ALBからのHTTPSリクエストをDjangoで信頼する
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://taishi-sushi.com', 'https://www.taishi-sushi.com']

# HTTPSを使用する場合のセキュリティ設定を追加
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False

# メール設定
AWS_SES_REGION_NAME = "ap-southeast-2"
AWS_SES_REGION_ENDPOINT = "email.ap-southeast-2.amazonaws.com"
EMAIL_BACKEND = "django_ses.SESBackend" #追加する
DEFAULT_FROM_EMAIL = "taishi03929@gmail.com" #追加する、@の後ろは取得したドメイン

# 静的ファイルとメディアファイルの設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'pages/static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# アプリケーションのその他の設定
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ses', # AWS SESの登録
    'pages',  # pagesアプリの登録
    'match',  # matchアプリの登録
    'trash_notifier', # trash_notifierアプリの登録
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mysite.context_processors.google_analytics',            # Google Analyticsに関しての設定
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Google Analytics設定
GOOGLE_ANALYTICS_TRACKING_ID = os.getenv('GOOGLE_ANALYTICS_TRACKING_ID', None)

# データベース設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワード検証
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ロケール設定
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# デフォルトのプライマリキー設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
