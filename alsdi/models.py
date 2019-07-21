from django.db import models
from .validators import validate_file_size



class Logo(models.Model):
    logo_name = models.CharField(max_length=255)
    image = models.ImageField(default='logos/default_logo.png', upload_to='logos')
    page = models.ForeignKey('alsdi.page', related_name='logo', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'شعار الموقع'
        verbose_name = 'شعار الموقع'

    def __str__(self):
        return self.logo_name

class NavbarLinks(models.Model):
    link_name = models.CharField(max_length=255)
    nav_link = models.CharField(max_length=255)
    page = models.ForeignKey('alsdi.page', related_name='navbar_links', on_delete=models.CASCADE, blank=True, null=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name_plural = 'روابط النافبار'
        verbose_name = 'روابط النافبار'
        ordering = ('weight',)

class Album(models.Model):
    album_name = models.CharField(max_length=255)
    section = models.ForeignKey('alsdi.Section', related_name='albums', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'البومات الصور'
        verbose_name = 'البومات الصور'

    def __str__(self):
        return self.album_name

class ImagesAlbum(models.Model):
    image_name = models.CharField(max_length=255)
    image = models.ImageField(default='album_images/default_image.png', upload_to='album_images')
    album = models.ForeignKey('alsdi.Album', related_name='image',on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = 'صور الالبومات'
        verbose_name = 'صور الالبومات'

class Slider(models.Model):
    slider_name = models.CharField(max_length=255)
    section = models.ForeignKey('alsdi.Section', related_name='sliders', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.slider_name

    class Meta:
        verbose_name_plural = 'سلايدر'
        verbose_name = 'سلايدر'
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
        verbose_name_plural = 'سلايد'
        verbose_name = 'سلايد'
        ordering = ('weight',)

class Page(models.Model):
    page_name = models.CharField(max_length=255)
    header = models.CharField(max_length=255, blank=True)
    paragraph = models.TextField(blank=True)
    page_language = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'الصفحات'
        verbose_name_plural = 'الصفحات'

    def __str__(self):
        return self.page_name

class Section(models.Model):
    section_header = models.CharField(max_length=255, blank=True)
    section_paragraph = models.TextField(blank=True)
    image = models.ImageField(upload_to='section_images', blank=True)
    page = models.ForeignKey('alsdi.Page', related_name='sections', on_delete=models.CASCADE, default="")
    weight = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'جزئية'
        verbose_name_plural = 'جزئية'
        ordering = ('weight',)

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
        verbose_name = 'بلوكات الجزئية'
        verbose_name_plural = 'بلوكات الجزئية'
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
    page = models.ManyToManyField('alsdi.Page', related_name='contact_us', blank=True)

    class Meta:
        verbose_name = 'عناوين التواصل'
        verbose_name_plural = 'عنواين التواصل'

    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_address = models.TextField()
    is_done = models.BooleanField(default=False)
    project_images = models.OneToOneField('alsdi.Album', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'المشاريع'
        verbose_name_plural = 'المشاريع'
        ordering = ('-date_created',)

    def __str__(self):
        return self.project_name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='articles_images', blank=True)
    page = models.ForeignKey('alsdi.Page', related_name='articles', default=1, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    is_new_article = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'اخر الاخبار'
        verbose_name_plural = 'اخر الاخبار'
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

class Booking(models.Model):
    email = models.EmailField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    project_subject = models.CharField(max_length=50, verbose_name="عنوان المشروع")
    project_type = models.CharField(max_length=50, verbose_name="نوع المشروع")
    project_quotation = models.CharField(max_length=50, verbose_name="نطاق التسعير")
    level = models.CharField(max_length=50, blank=True, null=True, verbose_name="مستوى التشطيب")
    date_sent = models.DateTimeField(auto_now=True, verbose_name="تاريخ الارسال")
    file1 = models.FileField(verbose_name="المخططات المعمارية", upload_to="booking_files", validators=[validate_file_size], default="default.png")
    file2 = models.FileField(verbose_name="المخططات الانشائية", upload_to="booking_files", validators=[validate_file_size], default="default.png")
    file3 = models.FileField(verbose_name="جداول الكميات", upload_to="booking_files", validators=[validate_file_size], default="default.png")
    file4 = models.FileField(verbose_name="المواصفات الفنية", upload_to="booking_files", validators=[validate_file_size], default="default.png")
    file5 = models.FileField(verbose_name="رخصة البناء", upload_to="booking_files", validators=[validate_file_size], default="default.png")

    class Meta:
        verbose_name = 'المواعيد'
        verbose_name_plural = 'المواعيد'
        ordering = ('-date_sent',)

    def __str__(self):
        return self.full_name


    
