from django.shortcuts import render
from appblog.models import Categoria, Post

def blog(request):
    pt=Post.objects.all() #traigo los objetos de la base de datos al post
    return render(request, 'blog.html', {"post":pt})

def categoria(request, categoria_id):
    category=Categoria.objects.get(id=categoria_id) #traigo y filtro las categorias de la BDD
    pt=Post.objects.filter(categorias=category) #traigo y filtro las categorias de la BDD
    
    return render(request, 'filtro.html', {"categoria":category, "post":pt,})
# Create your views here.
