from django.urls import path

from apponline import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('carteras/', views.carteras, name="carteras"),
    path('camperas/', views.camperas, name="camperas"),
    path('zapatos/', views.zapatos, name="zapatos"),
    path('accesorios/', views.accesorios, name="accesorios"),

    path('crear-carteras/', views.carteras_formulario, name="carteras_formulario"),
    path('busqueda-carteras-form/', views.busqueda_carteras, name="busqueda_carteras_form"),
    path('busqueda-carteras/', views.buscar_carteras, name="busqueda_carteras"),
    path('eliminar-cartera/<int:id>/', views.eliminar_cartera, name="eliminar_cartera"),
    path('editar-cartera/<int:id>/', views.editar_cartera, name="editar_cartera"),

    path('crear-camperas/', views.camperas_formulario, name="camperas_formulario"),
    path('busqueda-camperas-form/', views.busqueda_camperas, name="busqueda_camperas_form"),
    path('busqueda-camperas/', views.buscar_camperas, name="busqueda_camperas"),
    path('eliminar-campera/<int:id>/', views.eliminar_campera, name="eliminar_campera"),
    path('editar-campera/<int:id>/', views.editar_campera, name="editar_campera"),

    path('crear-zapatos/', views.zapatos_formulario, name="zapatos_formulario"),
    path('busqueda-zapatos-form/', views.busqueda_zapatos, name="busqueda_zapatos_form"),
    path('busqueda-zapatos/', views.buscar_zapatos, name="busqueda_zapatos"),
    path('eliminar-zapato/<int:id>/', views.eliminar_zapato, name="eliminar_zapato"),
    path('editar-zapato/<int:id>/', views.editar_zapato, name="editar_zapato"),

    path('crear-accesorios/', views.accesorios_formulario, name="accesorios_formulario"),
    path('busqueda-accesorios-form/', views.busqueda_accesorios, name="busqueda_accesorios_form"),
    path('busqueda-accesorios/', views.buscar_accesorios, name="busqueda_accesorios"),
    path('eliminar-accesorio/<int:id>/', views.eliminar_accesorio, name="eliminar_accesorio"),
    path('editar-accesorio/<int:id>/', views.editar_accesorio, name="editar_accesorio"),


#urls para login , registro y cerrar sesion
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),


#urls para editar perfil
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name='editar_perfil'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar_avatar'),
]
