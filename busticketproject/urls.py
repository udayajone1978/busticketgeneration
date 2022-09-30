"""busticketproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from onlineticket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_view),
    path('display/', views.display_view),
    path('update/<id>',views.update_view,name="update"),
    path('delete/<id>',views.delete_view),
    path('consumerdisplay/',views.consumerdisplay_view),
    path('consumer/',views.consumer_view),
    path('addconsumer/',views.consumer_view),
    path('deleteconsumer/<id>',views.deleteconsumer_view),
    path('updateconsumer/<id>',views.updateconsumer_view),
      ]

