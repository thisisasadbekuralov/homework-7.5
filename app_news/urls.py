from django.urls import path

from .views import NewsDetailView, NewsUpdateView, NewsListView, AddNewsView, NewsDeleteView, ListView, index

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='detail_news'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('add/', AddNewsView.as_view(), name='add_news'),
    path('update/<int:pk>', NewsUpdateView.as_view(), name='update_news'),
    path('send-mail/', index, name='send_mail')
]