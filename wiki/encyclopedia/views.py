from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown, Markdown
import random

from . import util

#Funcion que convierte el contenido de un archivo markdown a html
def md_to_html(titulo):
   contenido = util.get_entry(titulo)
   md = Markdown()  
   if contenido == None:
         return None
   else:
       return md.convert(contenido)   

#Funcion que va mostrar el contenido de una entrada o retornar un mensaje de error personalizado si la entrada no existe
def entrada(request, titulo):  
    contenido_html = md_to_html(titulo)
    if contenido_html == None:
        return render(request, "encyclopedia/error.html",{
            "mensaje": f"La entrada {titulo} no existe."
        })
    else:
        return render(request, "encyclopedia/entrada.html",{
            "titulo": titulo,
            "contenido": contenido_html
        
        })

#Funcion que nos va permitir buscar una determinada entrada, si no enconramos la entrada, vamos a retornar una lista con todas las entradas
#Relacionadas a esa palabra y al hacer click en alguna de ellas, nos va a redirigir a la pagina de la entrada seleccionada.
def busqueda(request):
    if request.method == "POST":
        busqueda = request.POST["q"]
        entrada_html = md_to_html(busqueda)
        if entrada_html is not None:
            return render(request, "encyclopedia/entrada.html",{
                "titulo": busqueda,
                "contenido": entrada_html
            })
        else:
            entradas_relacionadas = []
            entradas = util.list_entries()#Obtenemos todas las entradas
            for e in entradas: #Recorremos todas las entradas
                if busqueda.lower() in e.lower():
                    entradas_relacionadas.append(e)#Si la palabra buscada esta en alguna entrada, la agregamos a la lista de entradas relacionadas
            return render(request, "encyclopedia/busqueda.html",{
                "entradas": entradas_relacionadas
            })            
       
#Funcion que nos permitira agregar nuevas entradas
def agregar(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        contenido = request.POST['contenido']
        entradas = util.list_entries()
        if titulo in entradas:
            return render(request, "encyclopedia/error.html",{
                "mensaje": f"La entrada {titulo} ya existe en su directorio."
            })
        util.save_entry(titulo, contenido)
        return HttpResponseRedirect(reverse('entrada', args=[titulo]))#Redirigimos a la pagina de la entrada creada
    return render(request, "encyclopedia/agregar.html")#Si no se ha enviado un formulario, por defecto mostramos el formulario de agregar

#Funcion que nos va a permitir mostrar una entrada aleatoria segun las entradas que tengamos en nuestro directorio
def ramdon_entrada(request):
    entradas = util.list_entries()
    titulo = random.choice(entradas)
    return render(request, "encyclopedia/entrada.html",{
        "titulo": titulo,
        "contenido": md_to_html(titulo)
    
    })
  
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() 
    })

