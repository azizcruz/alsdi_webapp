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
    Project
    )

# Register your models here.

class NavbarAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'weight')
    list_editable = ('weight',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_name', 'weight')
    list_editable = ('weight',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'is_done', 'date_created')
    list_editable = ('is_done',)
    list_filter = ('is_done', 'date_created')


admin.site.register(Page)
admin.site.register(Logo)
admin.site.register(Contact)
admin.site.register(SectionBlock)
admin.site.register(Section)
admin.site.register(NavbarLinks, NavbarAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide)
admin.site.register(Album)
admin.site.register(ImagesAlbum)
admin.site.register(Project, ProjectAdmin)
