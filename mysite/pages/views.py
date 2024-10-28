from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'お問い合わせありがとうございます。')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

# thanks.html のviwes関数
class ThanksView(TemplateView):
    template_name = "pages/thanks.html"