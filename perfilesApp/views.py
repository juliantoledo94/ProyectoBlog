from loginApp.models import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from perfilesApp.forms import ProfilePageForm




class ShowProfilePageView(DetailView):
    model = Profile
    template_name='registration/user_profile.html'
    
    def get_context_data(self,*args, **kwargs):
        #user= Profile.objects.all()
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url','facebook_url','instagram_url']
    success_url= reverse_lazy('home')
    
    
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name= "registration/create_user_profile_page.html"
    #fields = '__all__'
    success_url= reverse_lazy('home')
    
    def form_valid(self,form):  
        form.instance.user = self.request.user
        return super().form_valid(form)
