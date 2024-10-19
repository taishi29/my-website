from django.contrib import admin
from .models import Company, CompanyImage

# Companyモデルを管理サイトに登録
admin.site.register(Company)
admin.site.register(CompanyImage)