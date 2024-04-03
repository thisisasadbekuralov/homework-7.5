from django.urls import path


from .views import AboutPageView, ContactPageView, CustomLogoutView

urlpatterns = [
    path('about-us/', AboutPageView.as_view(), name='about'),
    path('contact-us/', ContactPageView.as_view(), name='contact'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]