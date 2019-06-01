from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'pages', views.ListPages)
router.register(r'projects', views.ListProjects)

urlpatterns = [
    path('', include(router.urls))
]
