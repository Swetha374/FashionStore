"""fashionstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from fashionapi import views
from posts import views as pview
from store import views as sview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',views.HelloWorldView.as_view()),
    path('goodmorning/',views.GoodMorningView.as_view()),
    path('goodafternoon/',views.GoodAfternoonView.as_view()),
    path('greetings/',views.GreetingsView.as_view()),
    path("operations/cube/",views.CubeView.as_view()),
    path("operations/factorial/",views.FactorialView.as_view()),
    path("wordcount/",views.WordCountView.as_view()),
    path("social/posts/",pview.PostView.as_view()),
    path("social/posts/<int:pid>/",pview.PostDetailsView.as_view()),
    path("store/products/",sview.ProductsView.as_view()),
    path("store/products/<int:proid>/",sview.ProductDetailView.as_view()),

]
