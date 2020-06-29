from django.conf.urls import url, include

from users.views import login_success,fb_link,user_dashboard

urlpatterns = [
    url(r'^$', user_dashboard, name='user_dashboard'),
    url(r'^fb_link/', fb_link, name='fb_link'),


]
