"""fancybin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from pastes.views import home, newPaste, viewPaste, editPaste, savePaste, deletePaste

urlpatterns = [
    path('', home, name="home"),
    path('paste/new', newPaste, name="newpaste"),
    path('paste/view/<id>', viewPaste, name="viewpaste"),
    path('paste/edit/<id>', editPaste, name="editpaste"),
    path('paste/save/', savePaste, name="savepaste"),
    path('paste/delete/<id>', deletePaste, name="deletepaste"),
]
