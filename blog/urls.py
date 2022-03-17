from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('single/<slug:slug>', views.single, name="single"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('chart/', views.chart, name="chart"),
    path('form/', views.form, name="form"),
    path('errorpage/', views.error, name="error")
]
