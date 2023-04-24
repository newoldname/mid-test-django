"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views

urlpatterns = [
    # region FVB
    # path("<int:pk>/", views.single_post_page),
    # path("", views.index),
    # endrregion
    path("<int:pk>/add_comment/", views.new_comment),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("", views.PostList.as_view()),
    path("category/<str:slug>/", views.categories_page),
    path("tag/<str:slug>/", views.tags_page),
    path("create_post/", views.PostCreate.as_view()),
    path("update_post/<int:pk>/", views.PostUpdate.as_view()),
]
