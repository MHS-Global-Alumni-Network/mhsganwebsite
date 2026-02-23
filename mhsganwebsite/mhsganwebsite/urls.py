"""
URL configuration for mhsganwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from . import views
from chapters import views as chapters_views
from events import views as events_views
from posts import views as posts_views
from subscribers import views as subscribers_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('chapters/', chapters_views.chapters_list, name="chapters_list"),
    path('chapters/create/', chapters_views.create_chapter, name='create_chapter'),
    path('events/', events_views.events_list, name="events_list"),
    path('events/create/', events_views.create_event, name='create_event'),
    path('posts/', posts_views.posts_list, name="posts_list"),
    path('posts/create/', posts_views.create_post, name='create_post'),
    path('committees/', views.committees, name="committees"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('subscribe/', subscribers_views.create_subscriber, name='create_subscriber'),
    path('subscription_confirmation/', subscribers_views.confirm_subscription, name='confirm_subscription')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
