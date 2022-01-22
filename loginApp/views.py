
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

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
    
