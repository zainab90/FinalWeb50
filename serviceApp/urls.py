from django.urls import path

from serviceApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ShowService/<id>', views.show_service, name='show-service'),
    path('ViewBlog/<id>', views.view_blog, name='view-blog'),

]
