from django.urls import path
from .views import HomeView, PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:category>/', PostListView.as_view(), name='post_list'),
    path('<slug:category>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




