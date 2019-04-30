from django.db import models

class Logo(models.Model):
    logo_name = models.CharField(max_length=255)
    image = models.ImageField(default='logos/default_logo.png', upload_to='logos')

    def __str__(self):
        return self.logo_name

class NavbarLinks(models.Model):
    link_name = models.CharField(max_length=255)
    nav_link = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name_plural = 'navbar links'
        ordering = ('weight',)

class Slider(models.Model):
    slide = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousel_images', blank=True)
    header = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(blank=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.slide

    class Meta:
        verbose_name_plural = 'Slides'
        ordering = ('weight',)


class Page(models.Model):
    page_name = models.CharField(max_length=255)
    header = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(blank=True)

    def __str__(self):
        return self.page_name

class Section(models.Model):
    section_header = models.CharField(max_length=255, blank=True)
    section_paragraph = models.TextField(blank=True)
    image = models.ImageField(upload_to='section_images', blank=True)
    page = models.ForeignKey(Page, related_name='sections', on_delete=models.CASCADE, default="")
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.section_header

    class Meta:
        ordering = ('weight',)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=255, blank=True)
    facebook_address = models.CharField(max_length=255, blank=True)
    snapchat_address = models.CharField(max_length=255, blank=True)
    instgram_address = models.CharField(max_length=255, blank=True)
    twitter_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    telephone_number1 = models.CharField(max_length=255, blank=True)
    telephone_number2 = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

    