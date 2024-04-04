from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from config.settings import EMAIL_HOST_USER
from .models import News, Categories
from users.models import CustomUser


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

    def get_queryset(self):
        if 'keyword' in self.request.GET:
            queryset = (
                    News.objects.filter(news_title__icontains=self.request.GET['keyword']) |
                    News.objects.filter(news_description__icontains=self.request.GET['keyword']) |
                    News.objects.filter(news_content__icontains=self.request.GET['keyword'])
            )
        else:
            queryset = News.objects.all()
        if 'category' in self.request.GET:
            if self.request.GET["category"] != '0':
                queryset = queryset.filter(news_category=self.request.GET['category'])
        return queryset

class AddNewsView(LoginRequiredMixin, CreateView):
    template_name = 'news/add_news.html'
    model = News
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']
    success_url = '/'

    def form_valid(self, form):
        form.instance.news_author = self.request.user
        return super().form_valid(form)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'news/update_news.html'
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().news_author


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news/confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().news_author


def index(request):
    if request.method == 'POST':
        try:
            emails = CustomUser.objects.values_list('email', flat=True)
            subject = request.POST.get('subject', '')
            message = request.POST.get('text', '')
            print(emails)

            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=list(emails),
            )
            return HttpResponse('<h1>Email sent successfully!</h1>')
        except Exception as e:
            # Handle exceptions
            return HttpResponse('<h1>Something went wrong</h1><p>{}</p>'.format(e))

    return render(request, 'email_send.html')
