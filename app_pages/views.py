from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class CustomLogoutView(LogoutView):
    success_url = '/'