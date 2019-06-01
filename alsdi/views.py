from rest_framework.viewsets import ModelViewSet
from .models import Page, Project
from .serializers import PageSerializer, ProjectSerializer

class ListPages(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ListProjects(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer