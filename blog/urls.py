from django.urls import path, include
from . import views

urlpatterns = [
    path('Diagnostico/<int:pk>/', views.post_detail, name='post_detail'),
    path('Paciente/<int:pk>/', views.post_detail_pacient, name='post_detail_pacient'),
    path('Paciente/<int:pk>/edit/', views.post_edit_pacient, name='post_edit_pacient'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.intro, name='intro'),
    path('pacient', views.post_list_pacient, name='post_list_pacient'),
    path('Diagnostico/new', views.post_new, name='post_new'),
    path('Diagnostico/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('Paciente/new', views.post_new_pacient, name='post_new_pacient'),
]