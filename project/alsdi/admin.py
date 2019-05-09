from django.contrib import admin
from .models import (
    Page,
    Logo,
    NavbarLinks,
    Slider,
    Section,
    Contact, 
    SectionBlock, 
    )

# Register your models here.

class NavbarAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'weight')
    list_editable = ('weight',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('slide', 'weight')
    list_editable = ('weight',)


admin.site.register(Page)
admin.site.register(Logo)
admin.site.register(Contact)
admin.site.register(SectionBlock)
admin.site.register(Section)
admin.site.register(NavbarLinks, NavbarAdmin)
admin.site.register(Slider, SliderAdmin)
