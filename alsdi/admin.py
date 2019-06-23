from django.contrib import admin
from .models import (
    Page,
    Logo,
    NavbarLinks,
    Slider,
    Slide,
    Section,
    Contact, 
    SectionBlock,
    Album,
    ImagesAlbum,
    Project,
    Article
    )

# Register your models here.

class NavbarAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'weight')
    list_editable = ('weight',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_name', 'weight')
    list_editable = ('weight',)

class SlideAdmin(admin.ModelAdmin):
    list_filter = ('slider',)
    search_fields = ('header', 'paragraph')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'is_done', 'date_created')
    list_editable = ('is_done',)
    list_filter = ('is_done', 'date_created')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'date_created')
    list_filter = ('date_created',)

class SectionBlockAdmin(admin.ModelAdmin):
    list_filter = ('section',)
    search_fields = ('header', 'paragraph')


class ImageAlbumsAdmin(admin.ModelAdmin):
    list_filter = ('album',)



admin.site.register(Page)
admin.site.register(Logo)
admin.site.register(Contact)
admin.site.register(SectionBlock, SectionBlockAdmin)
admin.site.register(Section)
admin.site.register(NavbarLinks, NavbarAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Album)
admin.site.register(ImagesAlbum, ImageAlbumsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Article, ArticleAdmin)
