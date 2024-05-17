from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio),
    path('vistaAgregarGenero/', views.vistaAgregarGenero),
    path('agregarGenero/', views.agregarGenero),
    path('listarPeliculas/', views.listarPeliculas),
    path('vistaAgregarPelicula/', views.vistaAgregarPelicula),
    path('agregarPelicula/', views.agregarPelicula),
    path('consultarPelicula/<str:id>/', views.consultarPeliculaPorId),
    path('actualizarPelicula/', views.actualizarPelicula),
    path('eliminarPelicula/<str:id>/', views.eliminarPelicula),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
