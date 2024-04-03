
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pages/', include('app_pages.urls')),
    path('news/', include('app_news.urls')),
    path('', TemplateView.as_view(template_name='base.html')),

]
