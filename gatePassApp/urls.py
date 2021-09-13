from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
#     path('admin/', admin.site.urls),
    path('home/', views.home, name='homePage'),
    path('userProfile/<visitor_id>', views.profile, name='userProfile'),
    path('visitor/', views.visitor, name='visitor'),
    path('visitorAppoints/', views.visitorAppoints, name='visitorAppoints'),
    path('employeeAppoints/', views.employeeAppoints, name='employeeAppoints'),
    path('banned/', views.banned, name='banned'),
    path('cancelled/', views.cancelled, name='cancelled'),
    path('contractor/', views.contractor, name='contractor'),
    path('add-visitor/', views.addVisitor, name='add-visitor'),
    path('update-visitor/<str:pk>/', views.updateVisitor, name='update-visitor'),
    path('delete-visitor/<str:pk>/', views.deleteVisitor, name='delete-visitor'),
    path('add-contractor/', views.addContractor, name='add-contractor'),
    path('update-contractor/<str:pk>/',
         views.updateContractor, name='update-contractor'),
    path('delete-contractor/<str:pk>/',
         views.deleteContractor, name='delete-contractor'),
    path('visitor_text', views.visitor_text, name='visitor_text'),
    path('visitor_csv', views.visitor_csv, name='visitor_csv'),
    path('visitor_pdf', views.visitor_pdf, name='visitor_pdf'),
    path('contractor_text', views.contractor_text, name='contractor_text'),
    path('contractor_csv', views.contractor_csv, name='contractor_csv'),
    path('contractor_pdf', views.contractor_pdf, name='contractor_pdf'),
    path('all_events', views.all_events, name='all_events'),

]
