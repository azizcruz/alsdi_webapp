from rest_framework import serializers
from .models import Page, Section, Slider, Slide, Album, ImagesAlbum, Project

class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesAlbum
        fields = ('image',)

class AlbumSerializer(serializers.ModelSerializer):
    image = ImageAlbumSerializer(many=True, read_only=True)
    class Meta:
        depth = 1
        model = Album
        fields = ('album_name', 'image')

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('image', 'header', 'paragraph')

class SliderSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)
    class Meta:
        depth = 1
        model = Slider
        fields = ('slider_name', 'slides',)

class SectionSerializer(serializers.ModelSerializer):
    sliders = SliderSerializer(many=True, read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta:
        depth = 1
        model = Section
        fields = ('section_header', 'section_paragraph', 'image', 'sliders', 'blocks', 'albums')

class PageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        depth = 1
        model = Page
        fields = ('page_name', 'header', 'paragraph', 'sections',)

class ProjectSerializer(serializers.ModelSerializer):
    project_images = AlbumSerializer()
    class Meta:
        depth = 1
        model = Project
        fields = ('project_name', 'project_address', 'project_images', 'date_created')