from django.urls import path

from .views import login_view, logout_view, send_email_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('send-email/', send_email_view, name='send_email'),
]