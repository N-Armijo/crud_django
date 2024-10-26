from django.shortcuts import render,redirect, get_object_or_404
from .models import Tarea

# Vista para crear una tarea.
def crearTarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')#obtenemos el valor del formulario
        descripcion = request.POST.get('descripcion')
        #Creamos  la tarea en la base de datos
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        #######PARA REDIRIGIR USA EL NAME QUE DEFINIMOS EN EL URL####################################################
        return redirect('listar_tareas_me_llamo_name') #Redirige a la lista de tareas despues de crearla
    return render(request, 'create.html')#Mostrar el formulario en caso de GET

def listar_tareas(request):
    tareas = Tarea.objects.all()# obtiene todas las tareas desde la base de datos
    print(tareas)
    contexto = {'tareas': tareas}
    return render(request, 'listar_tareas.html', contexto )#pasamos las tareas al template

def actualizar_tarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    if request.method =='POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.save()#guarda los cambios en la base de datos
        return redirect('listar_tareas_me_llamo_name')
    return render(request, 'actualizar_tarea.html', {'tarea':tarea})

def eliminar_tarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    if request.method =='POST':
        tarea.delete()#Elimina la tarea de la base de datos
        return redirect('listar_tareas_me_llamo_name') #Rediirige a la lista despues de eliminar 
    return render(request, 'eliminar_tarea.html', {'tarea':tarea}) #Muestra el formulario de confirmacion

