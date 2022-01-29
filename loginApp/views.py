
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from loginApp.forms import FormularioPost
from .models import Post
from django.views import generic




def login(request):
     return render(request,"base.html")
 



class PostList(generic.ListView):
    queryset= Post.objects.filter(status=1).order_by("-created_on")
    template_name= "index.html"
    
    
class DetailView(generic.DetailView):
    model= Post
    template_name= "post_detail.html"




def Crear_post(request):
    
    if request.method == 'POST':
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post= Post.objects.create(
                title = form.cleaned_data["title"],
                slug = form.cleaned_data["slug"],
                author = form.cleaned_data["author"],
                
                content = form.cleaned_data["content"],
                status= form.cleaned_data["status"],
                imagen = form.cleaned_data["imagen"],
            )
            post.save()
            return redirect("home")
    else:
        form = FormularioPost()
    return render(request,"crear_post.html",{"form": form})
    

def busqueda_blog(request):
    return render(request,"busquedaBlog.html")

def buscar(request):
    # respuesta = f"Estoy buscando el titulo: {request.GET['title']}"
    # return HttpResponse(respuesta)
    if request.GET["title"]:
        title = request.GET['title']
        post= Post.objects.filter(title__icontains=title)
        
        return render(request,"resultadoBusquedaBlog.html",{"post":post, "title":title})
    
    else:
        respuesta ="No enviaste datos"
    return HttpResponse(respuesta)



def leer_post(request):
    post= Post.objects.all()
    contexto= {"post":post}
    
    return render(request,"leerPost.html",contexto)


def eliminar_post(request,post_title):
    post=Post.objects.get(title = post_title)
    post.delete()
    
    return redirect("home")




def update_post(request,post_title):
    
    post=Post.objects.get(title = post_title)
    
    if request.method == 'POST':
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            
            post.title = form.cleaned_data["title"]
            post.slug = form.cleaned_data["slug"]
            post.author = form.cleaned_data["author"]
                
            post.content = form.cleaned_data["content"]
            post.status= form.cleaned_data["status"]
            post.imagen = form.cleaned_data["imagen"]
            
            post.save()
            return redirect("home")
    else:
        form = FormularioPost(model_to_dict(post))
        
        
    return render(request,"crear_post.html",{"form": form})


