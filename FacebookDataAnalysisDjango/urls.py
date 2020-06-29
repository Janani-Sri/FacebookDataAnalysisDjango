"""FacebookDataAnalysisDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from FacebookDataAnalysisDjango import settings
from users.views import login_success,about

urlpatterns = [
    url(r'^$', login_success, name='login_success'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^login/$', auth_views.LoginView, name='login'),
    # url(r'^logout/$', auth_views.LogoutView, name='logout'),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/',include('allauth.urls'),name='facebook'),
    url(r'^admin/', admin.site.urls),
    url(r'^about_us/',about,name='about_us'),

    url(r'^user/', include('users.urls')),
    url(r'^sentiment/', include('sentiment.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)