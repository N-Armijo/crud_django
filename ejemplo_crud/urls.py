"""
URL configuration for ejemplo_crud project.

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
from mi_app.views import crearTarea
from mi_app.views import listar_tareas
from mi_app.views import actualizar_tarea
from mi_app.views import eliminar_tarea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',crearTarea, name='crear_tarea'),
    path('listar_tareas_soy_la_url',listar_tareas, name='listar_tareas_me_llamo_name'),
    path('actualizar/<int:id>',actualizar_tarea, name='actualizar_tarea'),
    path('eliminar/<int:id>',eliminar_tarea, name='eliminar_tarea'),
]
