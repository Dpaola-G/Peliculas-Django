from django.shortcuts import render, redirect
from django.db import Error
from appPeliculas.models import Genero, Pelicula
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from bson import ObjectId

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def vistaAgregarGenero(request):
    return render(request, "agregarGenero.html")


def agregarGenero(request):
    try:
        # recibir el nombre del genero en una variable local
        nombre = request.POST['txtNombre']
        # crear objeto de tipo genero
        genero = Genero(genNombre=nombre)
        # salvar el objeto, lo que permite que sea
        # creado en la base de datos
        genero.save()
        mensaje = "Genero Agregado Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    # return JsonResponse(retorno)
    return render(request, "agregarGenero.html", retorno)


def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas)  # para revisar en la consola
    retorno = {"peliculas": peliculas}
    return render(request, "listarPeliculas.html", retorno)


def vistaAgregarPelicula(request):
    generos = Genero.objects.all()
    retorno = {"generos": generos}
    return render(request, "agregarPelicula.html", retorno)


def agregarPelicula(request):
    try:
        codigo = request.POST['txtCodigo']
        titulo = request.POST['txtTitulo']
        protagonista = request.POST['txtProtagonista']
        duracion = int(request.POST['txtDuracion'])
        resumen = request.POST['txtResumen']
        foto = request.FILES['fileFoto']
        idGenero = ObjectId(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)
        # crear objeto pelicula
        pelicula = Pelicula(pelCodigo=codigo,
                            pelTitulo=titulo,
                            pelProtagonista=protagonista,
                            pelDuracion=duracion,
                            pelResumen=resumen,
                            pelFoto=foto,
                            pelGenero=genero)
        pelicula.save()
        mensaje = "Pelicula agregada correctamente"
        return redirect('/listarPeliculas/')
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje, 'idPelicula': pelicula.pk}
    # return JsonResponse(retorno)
    return render(request, "agregarPelicula.html", retorno)


def consultarPeliculaPorId(request, id):
    pelicula = Pelicula.objects.get(pk=ObjectId(id))
    generos = Genero.objects.all()
    # retornamos los generos porque se necesitan en la interfaz
    retorno = {"pelicula": pelicula, "generos": generos}
    return render(request, "actualizarPelicula.html", retorno)


def actualizarPelicula(request):
    try:
        idPelicula = ObjectId(request.POST['idPelicula'])
        # obtener la pelicula a partir de su id
        peliculaActualizar = Pelicula.objects.get(pk=idPelicula)
        # actualizar los campos
        peliculaActualizar.pelCodigo = request.POST['txtCodigo']
        peliculaActualizar.pelTitulo = request.POST['txtTitulo']
        peliculaActualizar.pelProtagonista = request.POST['txtProtagonista']
        peliculaActualizar.pelDuracion = int(request.POST['txtDuracion'])
        peliculaActualizar.pelResumen = request.POST['txtResumen']
        idGenero = ObjectId(request.POST['cbGenero'])
        # obtener el objeto Genero a partir de su id
        genero = Genero.objects.get(pk=idGenero)
        peliculaActualizar.pelGenero = genero
        foto = request.FILES.get('fileFoto')

        # si han enviado foto se actualiza el campo
        if (foto):
            # si la pelicula tiene foto debemos eliminarla
            if (peliculaActualizar.pelFoto != ""):
                # primero eliminamos la foto existente
                os.remove(os.path.join(settings.MEDIA_ROOT + "/" +
                                       str(peliculaActualizar.pelFoto)))
            # actualizamos con la nueva foto
            peliculaActualizar.pelFoto = foto

        # actualizar la pelicula en la base de datos
        peliculaActualizar.save()
        mensaje = "Pelicula Actualizada"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    # return JsonResponse(retorno)
    return redirect("/listarPeliculas")


def eliminarPelicula(request, id):
    try:
        # buscamos la pelicula por su id
        peliculaAEliminar = Pelicula.objects.get(pk=ObjectId(id))
        # Eliminamos la pelicula
        peliculaAEliminar.delete()
        mensaje = "Pelicula Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    # return JsonResponse(retorno)
    return redirect('/listarPeliculas')
