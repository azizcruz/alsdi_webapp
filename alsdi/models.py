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

class Album(models.Model):
    album_name = models.CharField(max_length=255)
    section = models.ForeignKey('alsdi.Section', related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name

class ImagesAlbum(models.Model):
    image_name = models.CharField(max_length=255)
    image = models.ImageField(default='album_images/default_image.png', upload_to='album_images')
    album = models.ForeignKey('alsdi.Album', related_name='image',on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = 'The images of the albums'

class Slider(models.Model):
    slider_name = models.CharField(max_length=255)
    section = models.ForeignKey('alsdi.Section', related_name='sliders', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.slider_name

    class Meta:
        verbose_name_plural = 'Sliders'
        ordering = ('weight',)

class Slide(models.Model):
    slider = models.ForeignKey('alsdi.Slider', related_name='slides', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carousel_images', blank=True)
    header = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(blank=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.header

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
    page = models.ForeignKey('alsdi.Page', related_name='sections', on_delete=models.CASCADE, default="")
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.section_header

class SectionBlock(models.Model):
    header = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(blank=True)
    image = models.ImageField(upload_to='section_images', blank=True)
    icon = models.CharField(max_length=255, blank=True)
    section = models.ForeignKey(Section, related_name='blocks', on_delete=models.CASCADE, default="")
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return self.header


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

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_address = models.TextField()
    is_done = models.BooleanField(default=False)
    project_images = models.OneToOneField('alsdi.Album', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_name
    