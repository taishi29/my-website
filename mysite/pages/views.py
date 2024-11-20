from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


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

# work.html のview関数
def work(request):
    params = {
    }
    return render(request, 'pages/work.html', params)


# contact.html のviwe関数
class ContactView(generic.FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        try:
            form.send_email()
            logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}")
            messages.error(self.request, "メール送信中にエラーが発生しました。")
            return self.form_invalid(form)
        
        messages.success(self.request, "お問い合わせ内容を送信しました！")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "入力内容にエラーがあります。確認して下さい。")
        return super().form_invalid(form)

# thanks.html のviwes関数
class ThanksView(TemplateView):
    template_name = "pages/thanks.html"


# health_check のviwe関数
def health_check(request):
    return HttpResponse("OK", status=200)
