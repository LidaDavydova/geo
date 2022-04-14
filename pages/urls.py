from django.urls import path, re_path
from . import views
from .views import *
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path('', TemplateView.as_view(template_name="base.html"), name='base')
]
