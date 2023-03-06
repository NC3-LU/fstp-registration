"""csskp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from survey import views

urlpatterns = [
    # Root
    path("", views.index, name="index"),
    path("terms/", views.get_terms, name="terms"),
    path("privacy/", views.get_privacy_policy, name="privacy"),
    # Stats
    path("stats/", include("stats.urls")),
    # Admin
    path("admin/", include("admin.urls")),
    path("admin/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    # Survey
    path("survey/", include("survey.urls")),
    # API
    path("api-auth/", include("rest_framework.urls")),
]
