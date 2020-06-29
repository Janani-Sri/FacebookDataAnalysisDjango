from django.urls import path
from . import views

urlpatterns = [
    path('pie-chart-sentiment/', views.sentiment_pie_chart, name='pie-chart-sentiment'),
    path('tag_cloud/', views.tag_cloud, name='tag_cloud'),
]