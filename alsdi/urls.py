from django.urls import path
from . import views

app_name = 'alsdi'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('our-services/', views.OurServices.as_view(), name='our-services'),
    path('about-us/', views.AboutUs.as_view(), name='about-us'),
    path('contact-us/', views.ContactUs.as_view(), name='contact-us'),
]

