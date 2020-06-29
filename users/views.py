import json

from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
import allauth
from allauth.socialaccount .models import SocialAccount,SocialToken,SocialApp
import facebook
import requests
from django.shortcuts import render, redirect
import urllib.request as urllib2
# Create your views here.

def user_dashboard(request):
    return render(request,'theme/admin/base.html')

def login_success(request):
    # data=SocialAccount.objects.get(user=request.user.id)
    # print(data.extra_data['link'])
    # data_token=SocialToken.objects.get(account=data.id)
    # print(data_token.account)
    # if(request.user.is_authenticated):
    #     try:
    #         data=SocialAccount.objects.get(user=request.user.id)
    #         pic=data.extra_data['link']
    #         uid=data.uid
    #         data_token = SocialToken.objects.get(account=data.id)
    #         token = data_token.token
    #         url = 'http://graph.facebook.com/2496044853944388/picture?'.format(uid)
    #         print(url)
    #         picture_url = "http://graph.facebook.com/{0}/picture?width=50&height=50&access;_token={1}".format(uid,token)
    #         # url = 'https://graph.facebook.com/{0}/picture&link&redirect=false&access;_token={1}'.format(uid,token)
    #         #
    #         # print(picture_url)
    #         return render(request, 'theme/landing_page/home.html',{data:url})
    #     except:
    #         pass
    try:
        data = SocialAccount.objects.get(user=request.user.id)
        uid=data.uid
        return render(request, 'theme/landing_page/home.html',{'uid':uid})
    except:
        pass
    return render(request, 'theme/landing_page/home.html')


def login(request):
    return render(request,'registration/login.html')


def fb_link(request):
    data=SocialAccount.objects.get(user=request.user.id)
    url= data.extra_data['link']

    return HttpResponseRedirect(url)
fb_link.attrs = {'target': '_blank'}

# class FacebookLink(RedirectView):
#     data = SocialAccount.objects.get(user=request.user.id)
#   url = 'https://google.com/?q=%(term)s'


def about(request):
    return render(request,'theme/landing_page/about.html')