from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Alumno,Genero
from django.contrib.auth.decorators import login_required

from .forms import GeneroForm

# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)

def anime(request):
    context={}
    return render(request, 'alumnos/anime.html', context)

def formulario(request):
    context={}
    return render(request, 'alumnos/formulario.html', context)

def nosotros(request):
    context={}
    return render(request, 'alumnos/nosotros.html', context)

def shopsingle(request):
    context={}
    return render(request, 'alumnos/shop-single.html', context)

def shopsingle2(request):
    context={}
    return render(request, 'alumnos/shop-single2.html', context)

def shopsingle3(request):
    context={}
    return render(request, 'alumnos/shop-single3.html', context)

def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context =  {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method is not "POST":

        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    
    else:

        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST[ "materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono = request.POST[ "telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"
        
        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    genero=genero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1 )
        obj.save() 
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'alumnos/alumnos_add.html', context)
    
def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        alumnos =  Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    
def alumnos_findEdit(request,pk):

    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno,'generos':generos}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)
        
def alumnosUpdate (request):
    if request.method == "POST" :
        #Es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla. |
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST[ "materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono = request.POST[ "telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno ()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1 
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'generos':generos,'alumno':alumno }
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)


def crud_generos(request):

    generos=Genero.objects.all()
    context ={'generos':generos}
    print("enviado datos generos_list")
    return render(request,"alumnos/generos_list.html",context)


def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpia form

            form=GeneroForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render (request,"alumnos/generos_add.html",context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'alumnos/generos_add.html', context)

def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'generos': generos, 'mensajes': mensajes, 'errores':errores}
            return render(request, 'alumnos/generos_list.html', context)
        
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'alumnos/generos_list.html', context)

def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontro el genero...")
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST,instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero': genero, 'form': form ,'mensaje': mensaje}
                return render(request, 'alumnos/generos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.object.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'generos':generos}
        return render(request, 'alumnos/generos_list.html', context)
