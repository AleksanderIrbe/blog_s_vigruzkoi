"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import render
import os
from gdrive import api



def render_post(request):
    google_scope = [
        # 'https://www.googleapis.com/auth/spreadsheets', # disabled
        'https://www.googleapis.com/auth/drive',
    ]
    doc_id = '17coS88dCReNY_psETrhNCvz39tFlsc7DUrkxFXwC7HA'

    gdrive_api = api.auth_in_google_drive(google_scope, os.getenv('GAPI_CREDENTIALS'))

    title, article_html = api.get_article_html(gdrive_api, doc_id)

    return render(request, template_name='post.html', context={'article_html':article_html, 'title':title})

urlpatterns = [
    path('', render, kwargs={
        'template_name': 'index.html',
    }),
    path('post/', render_post),
    path('category/', render, kwargs={
        'template_name': 'category.html',
    }),
    path('admin/', admin.site.urls),
]
