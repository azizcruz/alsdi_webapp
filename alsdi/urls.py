from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'pages', views.ListPages)
router.register(r'projects', views.ListProjects)
router.register(r'articles', views.ListArticles)

urlpatterns = [
    path('sendmail/', views.SendEmail.as_view(), name="send-mail"),
    path('newbooking/', views.BookingView.as_view(), name="booking"),
    path('', include(router.urls))
]
