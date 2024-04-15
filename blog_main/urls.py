
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('category/',include('blogs.urls')),
    path('blogs/<slug:slug>/',BlogViews.blogs, name='blogs'),
    path('blog/search/', BlogViews.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',include('dashboard.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
