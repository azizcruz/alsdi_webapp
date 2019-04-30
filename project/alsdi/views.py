from django.shortcuts import render, HttpResponse
from django.views import View
from .models import (Page, NavbarLinks, Logo, Slider, Contact, Section)
# Create your views here.

def get_navbar_link():
    return NavbarLinks.objects.all()
def get_site_logo():
    return Logo.objects.get(logo_name='شعارالموقع')
def get_footer_data():
    return Section.objects.get(section_header='عن  الشركة')


class Index(View):
    
    def get(self, request, *args, **kwargs):
        page = Page.objects.get(page_name='الرئيسية')
        slides = Slider.objects.all()
        context = {
            'page': page,
            'links': get_navbar_link(),
            'logo': get_site_logo(),
            'slides': slides,
            'footer': get_footer_data(),
            'title': 'الرئيسية'
        }
        return render(request, 'alsdi/index.html', context)

class OurServices(View):
    
    def get(self, request, *args, **kwargs):
        page = Page.objects.prefetch_related('sections').get(page_name='خدماتنا')
        context = {
            'page': page,
            'links': get_navbar_link(),
            'logo': get_site_logo(),
            'footer': get_footer_data(),
            'title': 'خدماتنا'
        }
        return render(request, 'alsdi/our_services.html', context)


class AboutUs(View):
    
    def get(self, request, *args, **kwargs):
        page = Page.objects.prefetch_related('sections').get(page_name='من نحن')
        context = {
            'page': page,
            'links': get_navbar_link(),
            'logo': get_site_logo(),
            'footer': get_footer_data(),
            'title': 'من نحن'
        }
        return render(request, 'alsdi/about_us.html', context)


class ContactUs(View):
    
    def get(self, request, *args, **kwargs):
        page = Page.objects.get(page_name='تواصل معنا')
        contact = Contact.objects.get(name='Alsdi Contact')
        context = {
            'page': page,
            'links': get_navbar_link(),
            'logo': get_site_logo(),
            'contact': contact,
            'footer': get_footer_data(),
            'title': 'تواصل معنا'
        }
        return render(request, 'alsdi/contact_us.html', context)
