from django.urls import path

from shiv import views
app_name = 'shiv'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('element/', views.element, name='element'),
    path('index1/', views.index1, name='index1')


]