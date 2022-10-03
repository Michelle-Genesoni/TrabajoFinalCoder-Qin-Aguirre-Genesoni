from inspect import Attribute
from tkinter import commondialog
from typing import Dict, Final

#Eliminar, editar, crear
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from django.http import HttpResponse
from django.template import loader


from apponline.models import Carteras, Camperas, Zapatos, Accesorios
from apponline.forms import CarterasFormulario, CamperasFormulario, ZapatosFormulario, AccesoriosFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def inicio(request):
      return render(request, "apponline/inicio.html")

def nosotros(request):
      return render(request, "apponline/nosotros.html")


def carteras(request):
      carteras = Carteras.objects.all()
      contexto = {"carteras": carteras}
      borrado = request.GET.get('borrado', None) 
      return render(request, "apponline/carteras.html", {'carteras': carteras})

@login_required
def eliminar_cartera(request, id):
    cartera = Carteras.objects.get(id=id)
    borrado_id = cartera.id
    cartera.delete()
    url_final = f"{reverse('carteras')}?borrado={borrado_id}"

    return redirect(url_final)

@login_required
def editar_cartera(request, id):
    cartera = Carteras.objects.get(id=id)

    if request.method == 'POST':
        formulario = CarterasFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            cartera.nombre = data['nombre']
            cartera.codigo = data['codigo']
            cartera.stock = data['stock']
            
            cartera.save()

            return redirect(reverse('carteras'))
    else:  # GET
        inicial = {
            'nombre': cartera.nombre,
            'codigo': cartera.codigo,
            'stock': cartera.stock,
        }
        formulario = CarterasFormulario(initial=inicial)
    return render(request, "apponline/form_carteras.html", {"formulario": formulario})
    

def camperas(request):
      camperas = Camperas.objects.all()
      return render(request, "apponline/camperas.html", {'camperas': camperas})
      
@login_required
def eliminar_campera(request, id):
    campera = Camperas.objects.get(id=id)
    borrado_id = campera.id
    campera.delete()
    url_final = f"{reverse('camperas')}?borrado={borrado_id}"

    return redirect(url_final)

@login_required
def editar_campera(request, id):
    campera = Camperas.objects.get(id=id)

    if request.method == 'POST':
        formulario = CamperasFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            campera.nombre = data['nombre']
            campera.codigo = data['codigo']
            campera.stock = data['stock']
            
            campera.save()

            return redirect(reverse('camperas'))
    else:  # GET
        inicial = {
            'nombre': campera.nombre,
            'codigo': campera.codigo,
            'stock': campera.stock,
        }
        formulario = CamperasFormulario(initial=inicial)
    return render(request, "apponline/form_camperas.html", {"formulario": formulario})


def zapatos(request):
      zapatos = Zapatos.objects.all()
      return render(request, "apponline/zapatos.html", {'zapatos': zapatos})

@login_required
def eliminar_zapato(request, id):
      zapato = Zapatos.objects.get(id=id)
      borrado_id = zapato.id
      zapato.delete()
      url_final = f"{reverse('zapatos')}?borrado={borrado_id}"

      return redirect(url_final)

@login_required
def editar_zapato(request, id):
    zapato = Zapatos.objects.get(id=id)

    if request.method == 'POST':
        formulario = ZapatosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            zapato.nombre = data['nombre']
            zapato.codigo = data['codigo']
            zapato.stock = data['stock']
            
            zapato.save()

            return redirect(reverse('zapatos'))
    else:  # GET
        inicial = {
            'nombre': zapato.nombre,
            'codigo': zapato.codigo,
            'stock': zapato.stock,
        }
        formulario = ZapatosFormulario(initial=inicial)
    return render(request, "apponline/form_zapatos.html", {"formulario": formulario})


def accesorios(request):
      accesorios = Accesorios.objects.all()
      return render(request, "apponline/accesorios.html",{'accesorios': accesorios})

@login_required
def eliminar_accesorio(request, id):
      accesorio = Accesorios.objects.get(id=id)
      borrado_id = accesorio.id
      accesorio.delete()
      url_final = f"{reverse('accesorios')}?borrado={borrado_id}"

      return redirect(url_final)

@login_required
def editar_accesorio(request, id):
    accesorio = Accesorios.objects.get(id=id)

    if request.method == 'POST':
        formulario = AccesoriosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            accesorio.nombre = data['nombre']
            accesorio.codigo = data['codigo']
            accesorio.stock = data['stock']
            
            accesorio.save()

            return redirect(reverse('accesorios'))
    else:  # GET
        inicial = {
            'nombre': accesorio.nombre,
            'codigo': accesorio.codigo,
            'stock': accesorio.stock,
        }
        formulario = AccesoriosFormulario(initial=inicial)
    return render(request, "apponline/form_accesorios.html", {"formulario": formulario})

# Formulario a mano
# def carteras_formulario(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             carteras = carteras(nombre=data_formulario['nombre'], codigo=data_formulario['codigo'])
#             carteras.save()
#             return render(request, "apponline/inicio.html")
#       else:  # GET
#             return render(request, "apponline/form_carteras.html")

@login_required 
def carteras_formulario(request):
      if request.method == 'POST':
            formulario= CarterasFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  carteras = Carteras(nombre=data['nombre'], codigo=data['codigo'],stock=data['stock']  )
                  carteras.save()
                  return render(request, "apponline/inicio.html", {"exitoso": True})
      else:  # GET
            formulario= CarterasFormulario()  # Formulario vacio para construir el html
      return render(request, "apponline/form_carteras.html", {"formulario": formulario})


@login_required 
def busqueda_carteras(request):
      return render(request, "apponline/form_busqueda_carteras.html")


@login_required 
def buscar_carteras(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            carteras = Carteras.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/carteras.html", {'carteras': carteras})
      else:
            return render(request, "apponline/carteras.html", {'carteras': []})

@login_required 
def camperas_formulario(request):
      if request.method == 'POST':
            formulario1= CamperasFormulario(request.POST)

            if formulario1.is_valid():
                  data = formulario1.cleaned_data
                  camperas = Camperas(nombre=data['nombre'], codigo=data['codigo'],stock=data['stock']  )
                  camperas.save()
                  return render(request, "apponline/inicio.html", {"exitoso": True})
      else:  # GET
            formulario1= CamperasFormulario()  # Formulario vacio para construir el html
      return render(request, "apponline/form_camperas.html", {"formulario": formulario1})

@login_required 
def busqueda_camperas(request):
            return render(request, "apponline/form_busqueda_camperas.html")

@login_required 
def buscar_camperas(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            camperas = Camperas.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/camperas.html", {'camperas': camperas})
      else:
            return render(request, "apponline/camperas.html", {'camperas': []})

@login_required 
def zapatos_formulario(request):
      if request.method == 'POST':
            formulario2= ZapatosFormulario(request.POST)

            if formulario2.is_valid():
                  data = formulario2.cleaned_data
                  zapatos = Zapatos(nombre=data['nombre'], codigo=data['codigo'],stock=data['stock']  )
                  zapatos.save()
                  return render(request, "apponline/inicio.html", {"exitoso": True})
      else:  # GET
            formulario2= ZapatosFormulario()  # Formulario vacio para construir el html
      return render(request, "apponline/form_zapatos.html", {"formulario": formulario2})

@login_required 
def busqueda_zapatos(request):
            return render(request, "apponline/form_busqueda_zapatos.html")

@login_required 
def buscar_zapatos(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            zapatos = Zapatos.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/zapatos.html", {'zapatos': zapatos})
      else:
            return render(request, "apponline/zapatos.html", {'zapatos': []})

@login_required 
def accesorios_formulario(request):
      if request.method == 'POST':
            formulario3= AccesoriosFormulario(request.POST)

            if formulario3.is_valid():
                  data = formulario3.cleaned_data
                  accesorios = Accesorios(nombre=data['nombre'], codigo=data['codigo'],stock=data['stock']  )
                  accesorios.save()
                  return render(request, "apponline/inicio.html", {"exitoso": True})
      else:  # GET
            formulario3= AccesoriosFormulario()  # Formulario vacio para construir el html
      return render(request, "apponline/form_accesorios.html", {"formulario": formulario3})

@login_required 
def busqueda_accesorios(request):
            return render(request, "apponline/form_busqueda_accesorios.html")

@login_required 
def buscar_accesorios(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            accesorios = Accesorios.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/accesorios.html", {'accesorios': accesorios})
      else:
            return render(request, "apponline/accesorios.html", {'accesorios': []})



#Views de usuarios, registro, login o logout

class CustomLogoutView(LogoutView):
      template_name = 'apponline/logout.html'
      next_page = reverse_lazy('login')


def register(request):
      mensaje = ''
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  form.save()
                  return render(request, "apponline/inicio.html", {"mensaje": "Usuario Creado :)"})

            else:
                  mensaje = 'Error al registrarse'
      formulario = UserRegisterForm()
      context = {"form": formulario}
      if mensaje:
            context['mensaje'] = mensaje 
      return render(request, "apponline/registro.html", context)


def login_request(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contraseña = form.cleaned_data.get('password')
                  user = authenticate(username=usuario, password=contraseña)

                  if user:
                        login(request=request, user=user) 
                        return render(request, "apponline/inicio.html", {"mensaje":f"Bienvenido a la tienda {usuario}"})                        
                  else:
                        return render(request, "apponline/inicio.html", {"mensaje": "Error, los datos ingresados son incorrectos :)"})
            else:
                  return render(request, "apponline/login.html", {"mensaje": "Error, los datos son incorrectos:)"})

      form = AuthenticationForm()
      return render(request, "apponline/login.html", {'form':form})


#Editar perfil del usuario

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
      model = User
      form_class = UserUpdateForm    
      success_url = reverse_lazy('inicio')
      template_name = "apponline/form_perfil.html"
      
      def get_object(self, queryset=None):
          return self.request.user 


def agregar_avatar(request):
    if request.method == 'POST':     
        form = AvatarFormulario(request.POST, request.FILES)  
        if form.is_valid:
            avatar = form.save()
            avatar.user = request.user 
            avatar.save()
            return redirect(reverse('inicio'))
    form = AvatarFormulario()
    return render(request, "apponline/form_avatar.html", {"form":form})










