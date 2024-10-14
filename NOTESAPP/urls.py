"""
URL configuration for NOTESAPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from note import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('create_notes/',views.create_notes,name='create_notes'),
    path('notes_list/',views.notes_list,name="notes_list"),
    path('update_and_save/<int:note_id>/',views.update_and_save,name='update_and_save'),
    path('delete_note/<int:note_id>/',views.delete_note,name='delete_note'),
    path('logout/',views.logout,name="logout"),
]
