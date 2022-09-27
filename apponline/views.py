from tkinter import commondialog
from typing import Dict

#Eliminar, editar, crear
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LogoutView

from django.http import HttpResponse
from django.template import loader


from apponline.models import Carteras, Camperas, Zapatos, Accesorios
from apponline.forms import CarterasFormulario, CamperasFormulario, ZapatosFormulario, AccesoriosFormulario, UserRegisterForm

#Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 

@login_required 
def inicio(request):
      return render(request, "apponline/inicio.html")


def carteras(request):
      carteras = Carteras.objects.all()
      contexto = {"carteras": carteras}
      borrado = request.GET.get('borrado', None) 
      return render(request, "apponline/carteras.html", {'carteras': carteras})


def camperas(request):
      camperas = Camperas.objects.all()
      return render(request, "apponline/camperas.html", {'camperas': camperas})


def zapatos(request):
      zapatos = Zapatos.objects.all()
      return render(request, "apponline/zapatos.html", {'zapatos': zapatos})


def accesorios(request):
      accesorios = Accesorios.objects.all()
      return render(request, "apponline/accesorios.html",{'accesorios': accesorios})


# Formulario a mano
# def carteras_formulario(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             carteras = carteras(nombre=data_formulario['nombre'], codigo=data_formulario['codigo'])
#             carteras.save()
#             return render(request, "apponline/inicio.html")
#       else:  # GET
#             return render(request, "apponline/form_carteras.html")


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



def busqueda_carteras(request):
      return render(request, "apponline/form_busqueda_carteras.html")



def buscar_carteras(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            carteras = Carteras.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/carteras.html", {'carteras': carteras})
      else:
            return render(request, "apponline/carteras.html", {'carteras': []})

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

def busqueda_camperas(request):
            return render(request, "apponline/form_busqueda_camperas.html")

def buscar_camperas(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            camperas = Camperas.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/camperas.html", {'camperas': camperas})
      else:
            return render(request, "apponline/camperas.html", {'camperas': []})

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

def busqueda_zapatos(request):
            return render(request, "apponline/form_busqueda_zapatos.html")

def buscar_zapatos(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            zapatos = Zapatos.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/zapatos.html", {'zapatos': zapatos})
      else:
            return render(request, "apponline/zapatos.html", {'zapatos': []})

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

def busqueda_accesorios(request):
            return render(request, "apponline/form_busqueda_accesorios.html")

def buscar_accesorios(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            accesorios = Accesorios.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/accesorios.html", {'accesorios': accesorios})
      else:
            return render(request, "apponline/accesorios.html", {'accesorios': []})


#Views de usuarios, registro, login o logout

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

class CustomLogoutView(LogoutView):
      template_name = 'apponline/logout.html'

      









